import json, re
d=json.load(open('ad_intel.json'))
lb=d['sales_leaderboard']
m=json.load(open('meta_ads.json'))

# meta spend lookup by ad_id and by ad_name
spend_by_id={a['ad_id']:(a.get('amount_spent') or 0) for a in m}
adset_by_id={a['ad_id']:a.get('ad_set_name') for a in m}

def concept(name):
    n=name.lower()
    if 'all the gear' in n or 'no idea' in n or 'p-b 002' in n or 'p-b 003'==n[:7]: 
        return 'All the Gear, No Idea'
    if 'more air bs' in n: return 'More Air BS'
    if "chops o'clock" in n or "chops o’clock" in n: return "Chops O'Clock"
    if 'unlock your trumpet potential' in n: return 'Unlock Your Trumpet Potential'
    if 'sax with captions' in n or 'sax captions' in n: return 'Sax with Captions'
    if 'tri tone' in n or 'tri-tone' in n: return 'Tri-tone (Longer Intro)'
    if 'hollywood bowl' in n: return 'Hollywood Bowl'
    if 'if force worked' in n: return 'If Force Worked'
    if 'misaligned musician' in n or 'not a bad trumpet player' in n: return 'Misaligned Musician'
    if 'coke can' in n: return 'Coke Can High G'
    if 'dino' in n or 'jurassic' in n: return 'Dino / Jurassic Park'
    if 'buzzing' in n: return 'Buzzing (Timo Organic)'
    if 'timo' in n and 'organic' in n: return 'Timo Organic Edit'
    if 'timo' in n: return 'Timo Organic Edit'
    if 'snow' in n: return 'Snow Angel'
    if 'evergreen with captions and text' in n or ('evergreen' in n and 'captions and text' in n): return 'Evergreen Captions+Text'
    if 'captions and trumpet players only' in n: return 'Captions + Trumpet-Players-Only'
    if '3 secrets' in n: return '3 Secrets'
    if 'triple g' in n or 'triple-g' in n or 'high g' in n: return 'Triple G / High G'
    if 'studio photo' in n or 'studio ad' in n or studio_like(n): return 'Studio Photo'
    if 'deer' in n or 'freedom deer' in n: return 'Deer on the Horn'
    if 'piccolo' in n: return 'Piccolo Captions'
    if 'salsa' in n: return 'Salsa Kingz Studio'
    if 'hollywood' in n: return 'Hollywood Bowl'
    if 'carousel' in n: return 'Carousel'
    if 'gig photo' in n or 'bar gig' in n: return 'Gig Photo'
    if 'stage' in n: return 'Stage Photo'
    if 'webinar photo' in n: return 'Webinar Photo'
    if 'trumpet pray' in n or 'pray no text' in n: return 'Trumpet Pray'
    if 'baja' in n or 'latin tune' in n or 'desert' in n: return 'Desert/Latin Tune'
    if 'kandy' in n: return 'Kandys Club Photo'
    if 'bungalow' in n: return 'Bungalow 8 Photo'
    if 'no captions' in n or 'no text' in n or 'captions and text' in n or 'captions and no text' in n or 'voice over' in n:
        return 'Generic Captions/Text variants'
    return 'Other / Misc'

def studio_like(n): return False

from collections import defaultdict
C=defaultdict(lambda:{'net':0.0,'sales':0,'calls':0,'variants':0,'spend':0.0,'names':[]})
for a in lb:
    c=concept(a['ad_name'])
    sp=a['spend'] or 0
    C[c]['net']+=a['net']; C[c]['sales']+=a['sales']; C[c]['calls']+=a['calls']
    C[c]['variants']+=1; C[c]['spend']+=sp; C[c]['names'].append((a['ad_name'],a['net'],a['sales'],a['calls'],sp))

rows=sorted(C.items(), key=lambda x:-x[1]['net'])
print('='*100)
print('RANKED CONCEPTS BY NET REVENUE')
print('='*100)
print(f\"{'CONCEPT':<32}{'NET$':>9}{'SALES':>6}{'CALLS':>6}{'VAR':>5}{'SPEND':>9}{'ROAS':>8}  s/call\")
for c,v in rows:
    roas = (v['net']/v['spend']) if v['spend']>0 else None
    rs = f\"{roas:.0f}x\" if roas else '-'
    sc = f\"{v['sales']/v['calls']:.0%}\" if v['calls'] else '-'
    print(f\"{c:<32}{v['net']:>9.0f}{v['sales']:>6}{v['calls']:>6}{v['variants']:>5}{v['spend']:>9.0f}{rs:>8}  {sc}\")

print()
print('CONCEPT MEMBERSHIP (net>0 concepts):')
for c,v in rows:
    if v['net']>0:
        print(f'\n## {c}  (net ${v[\"net\"]:.0f}, {v[\"sales\"]} sales)')
        for nm,net,s,ca,sp in sorted(v['names'],key=lambda x:-x[1]):
            if net>0 or sp>0:
                print(f'   {net:>8.0f} s{s} c{ca} sp{sp:.0f} | {nm}')
