// ADHD Dashboard. Reads state via <script> tag injection.
// file:// fetch is blocked in most browsers, so we use script-tag state hydration.
// derive.py writes state/tasks.js as `window.TASKS_STATE = {...}`.

const STATE_SCRIPT = '../state/tasks.js';
const HOUR_START = 6;
const HOUR_END = 23;
const POLL_MS = 60 * 1000;

const $ = (id) => document.getElementById(id);

function fmtDay(jstStr) {
  if (!jstStr) return '';
  const [y, m, d] = jstStr.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const mos = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  return `${days[dt.getUTCDay()]} ${mos[dt.getUTCMonth()]} ${dt.getUTCDate()}`;
}

function jstNow() {
  // Return a Date whose UTC-methods (getUTCHours, etc) yield JST values.
  return new Date(Date.now() + 9 * 60 * 60 * 1000);
}
function hoursUntil(deadlineJst) {
  if (!deadlineJst) return Infinity;
  const [y, m, d] = deadlineJst.split('-').map(Number);
  // Deadline at end of day JST = 14:59 UTC.
  const dlUtcMs = Date.UTC(y, m - 1, d, 14, 59, 0);
  return (dlUtcMs - Date.now()) / (1000 * 60 * 60);
}

function daysSince(iso) {
  if (!iso) return 0;
  const then = new Date(iso);
  return Math.floor((Date.now() - then.getTime()) / (1000 * 60 * 60 * 24));
}

function renderTimeline(data) {
  const tl = $('timeline');
  tl.innerHTML = '';

  // hour rows
  for (let h = HOUR_START; h < HOUR_END; h++) {
    const row = document.createElement('div');
    row.className = 'timeline-hour';
    row.style.top = `${(h - HOUR_START) * 60}px`;
    const label = document.createElement('div');
    label.className = 'th-label';
    const ampm = h < 12 ? 'am' : 'pm';
    const hh = h === 0 ? 12 : h > 12 ? h - 12 : h;
    label.textContent = `${hh}${ampm}`;
    row.appendChild(label);
    const slot = document.createElement('div');
    slot.className = 'th-slot';
    row.appendChild(slot);
    tl.appendChild(row);
  }

  // NOW line (JST)
  const j = jstNow();
  const jstH = j.getUTCHours() + j.getUTCMinutes() / 60;
  if (jstH >= HOUR_START && jstH <= HOUR_END) {
    const line = document.createElement('div');
    line.className = 'now-line';
    line.style.top = `${(jstH - HOUR_START) * 60}px`;
    tl.appendChild(line);
  }

  const todayTasks = (data.buckets && data.buckets.today) || [];
  const timeboxed = todayTasks.filter(t => t.start_hour != null);

  if (timeboxed.length === 0) {
    const empty = document.createElement('div');
    empty.className = 'timeline-empty';
    empty.innerHTML = `nothing timeboxed today.<br>populate via <code>/task add "..." --start HH --est MIN --deadline ${data.today_jst || 'YYYY-MM-DD'}</code>`;
    tl.appendChild(empty);
    return;
  }

  for (const t of timeboxed) {
    const blk = document.createElement('div');
    blk.className = `task-block tier-${t.tier || 'T2'}`;
    if (t.started_at && !t.completed_at) blk.classList.add('started');
    if (t.status === 'completed') blk.classList.add('completed');

    const startOffset = t.start_hour - HOUR_START;
    const dur = t.estimated_min || 30;
    blk.style.setProperty('--start-offset', startOffset);
    blk.style.setProperty('--dur-min', dur);
    blk.style.top = `${startOffset * 60}px`;
    blk.style.height = `${Math.max(28, dur * 1)}px`;

    const check = document.createElement('div');
    check.className = 'tb-check';
    check.textContent = t.status === 'completed' ? '.' : '';
    if (t.status === 'completed') check.textContent = '\u2713';
    blk.appendChild(check);

    const title = document.createElement('div');
    title.className = 'tb-title';
    title.textContent = t.title;
    blk.appendChild(title);

    const meta = document.createElement('div');
    meta.className = 'tb-meta';
    meta.innerHTML = `<span>${dur}m</span><span>${t.project || ''}</span>`;
    blk.appendChild(meta);

    tl.appendChild(blk);
  }
}

function sideTaskEl(t, opts = {}) {
  const el = document.createElement('div');
  el.className = 'side-task';
  if (opts.urgencyClass) el.classList.add(opts.urgencyClass);
  const title = document.createElement('div');
  title.className = 'st-t';
  title.textContent = t.title;
  el.appendChild(title);
  const meta = document.createElement('div');
  meta.className = 'st-m';
  const bits = [];
  if (t.project) bits.push(`<span>${t.project}</span>`);
  if (t.tier) bits.push(`<span class="tag ${t.tier === 'T1' ? 'tg' : t.tier === 'T2' ? 'to' : 'tp'}">${t.tier}</span>`);
  if (opts.extra) bits.push(opts.extra);
  meta.innerHTML = bits.join('');
  el.appendChild(meta);
  return el;
}

function renderPanel(id, items, renderItem, emptyText) {
  const el = $(id);
  el.innerHTML = '';
  if (!items || items.length === 0) {
    const e = document.createElement('div');
    e.className = 'empty-note';
    e.textContent = emptyText;
    el.appendChild(e);
    return;
  }
  for (const item of items) el.appendChild(renderItem(item));
}

function renderDashboard(data) {
  const b = data.buckets || {};

  $('today-label').textContent = `${fmtDay(data.today_jst)} (${data.today_jst || ''})`;
  $('stat-today').textContent = (b.today || []).length;
  $('stat-dl').textContent = (b.deadlines_72h || []).length;
  $('stat-blocked').textContent = (b.blocked || []).length;
  $('stat-shipped').textContent = (b.shipped_today || []).length;
  $('event-count').textContent = `${data.event_count || 0} events, ${data.task_count || 0} tasks`;
  $('refresh-ts').textContent = `refreshed ${new Date().toLocaleTimeString('en-US', { hour12: false })}`;

  renderTimeline(data);

  // Deadlines 72h. urgent if under 24h
  renderPanel('panel-dl', b.deadlines_72h, (t) => {
    const h = hoursUntil(t.deadline_jst);
    const cls = h < 0 ? 'urgent' : h < 24 ? 'urgent' : h < 48 ? 'soon' : '';
    const whenLabel = h < 0 ? `<span class="tag tr">OVERDUE</span>` :
      h < 24 ? `<span class="tag tr">${Math.max(0, Math.floor(h))}h left</span>` :
      `<span class="tag ty">${Math.floor(h / 24)}d ${Math.floor(h % 24)}h</span>`;
    return sideTaskEl(t, { urgencyClass: cls, extra: whenLabel });
  }, 'no deadlines within 72h. breathe.');

  renderPanel('panel-blocked', b.blocked, (t) =>
    sideTaskEl(t, { extra: t.blocked_on ? `<span class="st-m-sub">blocked: ${t.blocked_on}</span>` : '' })
  , 'nothing blocked.');

  renderPanel('panel-shipped-today', b.shipped_today, (t) =>
    sideTaskEl(t, { extra: t.shipped ? `<span class="tag tg">${t.shipped}</span>` : '<span class="tag tg">done</span>' })
  , 'nothing shipped today yet. go do the thing.');

  renderPanel('panel-shipped-week', b.shipped_week, (t) =>
    sideTaskEl(t, { extra: t.completed_at ? `<span>${(t.completed_at || '').slice(5, 10)}</span>` : '' })
  , 'nothing shipped this week.');

  renderPanel('panel-stale', b.stale, (t) => {
    const d = daysSince(t.last_touched);
    return sideTaskEl(t, { extra: `<span class="tag to">${d}d untouched</span>` });
  }, 'no stale tasks.');

  renderPanel('panel-parked', b.parked, (t) => sideTaskEl(t), 'nothing parked.');
}

function load(isInitial) {
  if (isInitial && window.TASKS_STATE) {
    renderDashboard(window.TASKS_STATE);
    return;
  }
  // Swap the state script tag with a fresh cache-busted version.
  const old = $('state-script');
  const next = document.createElement('script');
  next.id = 'state-script';
  next.src = `${STATE_SCRIPT}?t=${Date.now()}`;
  next.onload = () => {
    if (window.TASKS_STATE) renderDashboard(window.TASKS_STATE);
    else $('today-label').textContent = 'state load error: window.TASKS_STATE missing';
  };
  next.onerror = () => {
    $('today-label').textContent = 'state load error: could not read ../state/tasks.js';
  };
  if (old && old.parentNode) old.parentNode.replaceChild(next, old);
  else document.body.appendChild(next);
}

// Collapse toggles
document.addEventListener('DOMContentLoaded', () => {
  const toggle = (btnId, panelId) => {
    const btn = $(btnId); const panel = $(panelId);
    if (!btn || !panel) return;
    btn.addEventListener('click', () => {
      const collapsed = panel.classList.toggle('card-collapsed');
      btn.textContent = collapsed ? '[expand]' : '[collapse]';
    });
  };
  toggle('expand-week', 'panel-shipped-week');
  toggle('expand-parked', 'panel-parked');

  load(true);
  setInterval(() => load(false), POLL_MS);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) load(false);
  });
});
