from PIL import Image, ImageDraw, ImageFont
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
J="/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
f=lambda p,s:ImageFont.truetype(p,s)
NAVY=(11,22,52); ACC=(120,190,255); W,H=1080,1350
def wrap(d,t,font,mw):
    out=[]
    for para in t.split("\n"):
        cur=""
        for w in para.split():
            x=(cur+" "+w).strip()
            if d.textlength(x,font=font)<=mw: cur=x
            else: out.append(cur); cur=w
        out.append(cur)
    return out
def slide(path,kicker,title,body="",num=None,cta=False,quote=False):
    img=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(img)
    d.rectangle([40,40,W-40,H-40],outline=ACC,width=4)
    d.text((80,90),kicker,font=f(B,32),fill=ACC)
    d.text((W-80,70),"絆",font=f(J,90),fill=(40,60,110),anchor="ra")
    tf=f(B,80 if not quote else 64); bf=f(R,40)
    tl=wrap(d,title,tf,W-160); bl=wrap(d,body,bf,W-160) if body else []
    th=len(tl)*int(tf.size*1.2); bh=len(bl)*58
    numh=190 if num else 0
    total=numh+th+(50 if body else 0)+bh
    bottom=H-230 if cta else H-120
    y=170+((bottom-170)-total)//2
    if num:
        d.ellipse([80,y,230,y+150],fill=ACC); d.text((155,y+75),str(num),font=f(B,84),fill=NAVY,anchor="mm"); y+=190
    for l in tl: d.text((80,y),l,font=tf,fill="white"); y+=int(tf.size*1.2)
    if body:
        y+=50
        for l in bl: d.text((80,y),l,font=bf,fill=(205,220,240)); y+=58
    if cta:
        d.rectangle([40,H-200,W-40,H-40],fill=ACC)
        d.text((W//2,H-145),"DM us or send your link at",font=f(B,36),fill=NAVY,anchor="mm")
        d.text((W//2,H-90),"kizunaproxy.com",font=f(B,46),fill=NAVY,anchor="mm")
    else:
        d.text((W-80,H-80),"kizunaproxy.com",font=f(B,30),fill=ACC,anchor="rs")
    img.save(path,quality=92)
P="/home/claude/kizuna-posts/images/evergreen/"
# 1 How it works
slide(P+"how-1.jpg","HOW IT WORKS","Buy anything from Japan. Even in-store only items.","Here's how Kizuna Proxy gets it to your door in 3 steps →")
slide(P+"how-2.jpg","STEP 1","Send us what you want","A Mercari or Yahoo Auctions link, a shop page, or just a photo of a pop-up item.",num=1)
slide(P+"how-3.jpg","STEP 2","We quote & buy it for you","Online, or in person in Tokyo stores, pop-ups and events. No Japanese needed on your side.",num=2)
slide(P+"how-4.jpg","STEP 3","We pack it with care & ship worldwide","Bubble wrap, sturdy boxes, tracked shipping to your country.",num=3)
slide(P+"how-5.jpg","READY?","Tell us what you're looking for","We answer every request personally.",cta=True)
# 2 What we can get
slide(P+"what-1.jpg","WHAT WE CAN GET FOR YOU","If it's sold in Japan, we can probably get it.","Swipe to see where we shop →")
slide(P+"what-2.jpg","ONLINE","Japanese marketplaces","Mercari · Yahoo Auctions · Rakuten · Japan-only web shops that don't ship abroad.")
slide(P+"what-3.jpg","IN STORE · TOKYO","Pop-ups, events & limited merch","Exclusive goods only sold on site: anime pop-ups, collab cafés, idol & K-pop events.")
slide(P+"what-4.jpg","RARE FINDS","Collectibles & hard-to-find items","Trading cards, vintage, handmade pieces. We search second-hand shops for you.")
slide(P+"what-5.jpg","LOOKING FOR SOMETHING?","Send us the item — we'll find a way.","",cta=True)
# 3 Reviews
slide(P+"rev-1.jpg","WHAT CUSTOMERS SAY","Rated 4.7 ★ on Trustpilot","Real reviews from real customers →")
slide(P+"rev-2.jpg","CUSTOMER REVIEW","“10/10 would recommend and repeat business”","K-pop photocards from a Japanese resale platform",quote=True)
slide(P+"rev-3.jpg","CUSTOMER REVIEW","“Amazing proxy for items in Japan!”","Limited pop-up items from Shibuya 109 — first time using a proxy",quote=True)
slide(P+"rev-4.jpg","CUSTOMER REVIEW","“Super friendly!”","Items only sold in physical stores, packed securely in bubble wrap",quote=True)
slide(P+"rev-5.jpg","YOUR TURN","Join our happy customers","",cta=True)
