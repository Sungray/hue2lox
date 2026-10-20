"""Build a factual snapshot from the upstream Philips device definitions; no code execution."""
import csv,hashlib,json,re,sys
from pathlib import Path
source=Path(sys.argv[1]);root=Path(__file__).resolve().parent.parent
expected='96b02d51956f47dab2bf9f0e5ada7f2d56902a27873724d3dd2539af2b59a2c5'
if hashlib.sha256(source.read_bytes()).hexdigest()!=expected:
    raise SystemExit('Source differs from pinned upstream snapshot; update provenance explicitly before regenerating.')
text=source.read_text();rows=[]
for block in re.findall(r'^    \{\n(.*?)^    \},',text,re.M|re.S):
    light=bool(re.search(r'(?:philips\.m|m)\.light\(',block))
    plug='Hue smart plug' in block or 'Hue Smart plug' in block
    if not light and not plug:continue
    ids=re.search(r'zigbeeModel:\s*\[(.*?)\]',block,re.S)
    model=re.search(r'^        model: "([^"]+)"',block,re.M)
    desc=re.search(r'^        description: "([^"]+)"',block,re.M)
    if not ids or not model or not desc:continue
    caps=['on']
    if light:caps.append('brightness')
    if light and re.search(r'colorTemp:\s*(?:true|\{)',block):caps.append('temperature')
    if light and re.search(r'\bcolor:\s*(?:true|\{)',block):caps.append('rgb')
    for identifier in re.findall(r'"([^"]+)"',ids[1]):
        rows.append({'model_id':identifier,'product_id':model[1],'name':desc[1],'capabilities':caps,'gradient':'gradient: true' in block})
rows.sort(key=lambda row:(row['model_id'],row['product_id']))
meta={'source_commit':'499535e092401a6c21e8c3b5e3aeca8062c11841','source':'https://github.com/Koenkk/zigbee-herdsman-converters/blob/499535e092401a6c21e8c3b5e3aeca8062c11841/src/devices/philips.ts','retrieved':'2026-10-18','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'coverage':'All light and Hue plug definitions with zigbeeModel in this source snapshot; not a complete official worldwide Hue catalog. Bridge capabilities take precedence.','models':rows}
(root/'catalog/hue-models.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
with (root/'catalog/hue-models.csv').open('w',newline='') as f:
    writer=csv.writer(f,lineterminator="\n");writer.writerow(['model_id','product_id','name','on_off','dimmer','tunable_white','rgb','gradient','source'])
    for row in rows:writer.writerow([row['model_id'],row['product_id'],row['name'],True,'brightness' in row['capabilities'],'temperature' in row['capabilities'],'rgb' in row['capabilities'],row['gradient'],meta['source']])
print(len(rows),'model rows')
