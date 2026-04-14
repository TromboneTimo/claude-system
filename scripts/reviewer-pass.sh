#!/usr/bin/env bash
# reviewer-pass.sh: capture BEFORE/AFTER state of a skill/memory file for
# feeding to the skill-reviewer subagent.
#
# Usage:
#   reviewer-pass.sh capture <file>      # saves current state as BEFORE
#   reviewer-pass.sh diff <file>         # compares current state against last BEFORE
#   reviewer-pass.sh from-git <file> <old-commit> [new-commit]
#                                        # extracts BEFORE/AFTER from git history
#
# After capture + diff, invoke the skill-reviewer agent in Claude with:
#   "Run reviewer pass on <file>. BEFORE: /tmp/reviewer-state/<name>.before.md
#    AFTER: <file>. Pointers: <list any new references added>."

set -euo pipefail

STATE_DIR="/tmp/reviewer-state"
mkdir -p "$STATE_DIR"

cmd="${1:-help}"

case "$cmd" in
  capture)
    file="${2:?need file path}"
    [ -f "$file" ] || { echo "ERROR: $file not found"; exit 1; }
    name=$(basename "$file")
    cp "$file" "$STATE_DIR/$name.before.md"
    wc -l "$file" "$STATE_DIR/$name.before.md"
    echo "Captured BEFORE. Make your edits, then run: $0 diff $file"
    ;;

  diff)
    file="${2:?need file path}"
    name=$(basename "$file")
    before="$STATE_DIR/$name.before.md"
    [ -f "$before" ] || { echo "ERROR: no BEFORE captured. Run: $0 capture $file"; exit 1; }
    echo "=== Line count delta ==="
    wc -l "$before" "$file"
    echo ""
    echo "=== Diff (unified, 3 lines context) ==="
    diff -u "$before" "$file" || true
    echo ""
    echo "=== New pointer references in AFTER ==="
    grep -nE '(~/\.claude/knowledge/|feedback_[a-z_]+\.md|references/)' "$file" | head -20 || echo "(none)"
    echo ""
    echo "Next: invoke skill-reviewer subagent with these paths:"
    echo "  BEFORE: $before"
    echo "  AFTER:  $file"
    ;;

  from-git)
    file="${2:?need file path relative to ~/.claude}"
    old="${3:?need old commit hash}"
    new="${4:-HEAD}"
    name=$(basename "$file")
    cd "$HOME/.claude"
    git show "$old:$file" > "$STATE_DIR/$name.before.md" 2>/dev/null || { echo "ERROR: cannot extract $file at $old"; exit 1; }
    git show "$new:$file" > "$STATE_DIR/$name.after.md" 2>/dev/null || { echo "ERROR: cannot extract $file at $new"; exit 1; }
    echo "=== Line count delta ==="
    wc -l "$STATE_DIR/$name.before.md" "$STATE_DIR/$name.after.md"
    echo ""
    echo "Ready for skill-reviewer subagent:"
    echo "  BEFORE: $STATE_DIR/$name.before.md  (commit $old)"
    echo "  AFTER:  $STATE_DIR/$name.after.md   (commit $new)"
    ;;

  clean)
    rm -rf "$STATE_DIR"/*.md 2>/dev/null || true
    echo "Cleaned $STATE_DIR"
    ;;

  help|*)
    cat <<USAGE
reviewer-pass.sh: capture BEFORE/AFTER for skill/memory compactions

Commands:
  capture <file>                  Save current state as BEFORE (before editing)
  diff <file>                     Compare current state to last captured BEFORE
  from-git <file> <old> [<new>]   Extract BEFORE/AFTER from git (for retrospective review)
  clean                           Remove all captured state

Typical workflow:
  1. $0 capture ~/.claude/skills/my-skill/SKILL.md
  2. (edit the file)
  3. $0 diff ~/.claude/skills/my-skill/SKILL.md
  4. In Claude: invoke skill-reviewer subagent with the BEFORE/AFTER paths

Retrospective workflow (audit past commits):
  $0 from-git skills/my-skill/SKILL.md abc1234 def5678
  (then invoke skill-reviewer with the output paths)

State stored in: $STATE_DIR
USAGE
    ;;
esac
