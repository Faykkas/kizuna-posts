import sys
from PIL import Image, ImageDraw, ImageFont
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
J="/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
f=lambda p,s:ImageFont.truetype(p,s)
NAVY=(11,22,52)
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def card(out,title,sub,rows,acc):
    W=H=1080; img=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(img)
    d.rectangle([40,40,W-40,H-40],outline=acc,width=4)
    d.text((80,90),"POP-UP ALERT  ·  TOKYO",font=f(B,34),fill=acc)
    d.text((W-80,70),"絆",font=f(J,90),fill=(40,60,110),anchor="ra")
    size=88
    while True:
        tf=f(B,size); lines=wrap(d,title,tf,W-160)
        if len(lines)<=3 or size<=60: break
        size-=6
    blockh=len(lines)*int(size*1.22)+100+36+len(rows)*62
    y=170+((H-230-170)-blockh)//2
    for l in lines: d.text((80,y),l,font=tf,fill="white"); y+=int(size*1.22)
    d.text((80,y+8),sub,font=f(B,42),fill=acc); y+=100
    d.line([80,y,W-80,y],fill=acc,width=2); y+=36
    for lab,val in rows:
        d.text((80,y+4),lab,font=f(B,28),fill=acc); d.text((260,y),val,font=f(R,34),fill="white"); y+=62
    d.rectangle([40,H-200,W-40,H-40],fill=acc)
    d.text((W//2,H-145),"Can't be in Tokyo? We'll buy it for you.",font=f(B,36),fill=NAVY,anchor="mm")
    d.text((W//2,H-90),"kizunaproxy.com",font=f(B,46),fill=NAVY,anchor="mm")
    img.save(out,quality=92)
cards=[
 ("images/2026-11-bocchi-akihabara.jpg","Bocchi the Rock!","POP UP SHOP · WINTER 2026",
  [("DATES","Nov 13 – 26, 2026"),("WHERE","atre Akihabara"),("BONUS","Limited gift with purchase")],(255,150,190)),
 ("images/2026-11-miku-shibuya.jpg","Hatsune Miku Magical Mirai 2026","POP UP SHOP",
  [("DATES","Nov 3 – 30, 2026"),("WHERE","SHIBUYA TSUTAYA · 6F"),("BONUS","Exclusive bromide / ¥3,300")],(90,220,210)),
 ("images/2026-11-tokrev-shinjuku.jpg","Tokyo Revengers","POP-UP SHOP",
  [("DATES","Nov 14 – 23, 2026"),("WHERE","Shinjuku Marui Annex · 2F"),("BONUS","Bromides & acrylic art")],(255,190,90)),
 ("images/2026-11-chiikawa-ikebukuro.jpg","Chiikawa Pocket","POP UP STORE #4",
  [("DATES","Oct 24 – Nov 23, 2026"),("WHERE","Ikebukuro PARCO · 6F"),("ITEMS","New exclusive goods")],(150,200,255)),
]
for c in cards: card(*c)
