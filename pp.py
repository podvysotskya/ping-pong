# ping-pong
bx=285
by=150
bxs=0
bys=0
rx=10
ry=100
rx2=540
ry2=100
il=0
ir=0
p1=320
p2=320
p3=320
p4=320
p5=320
p6=320
def setup():
    size(600,400)
def draw():
    global bx,by,bxs,bys,rx,ry,rx2,ry2,i,il,ir,p1,p2,p3,p4,p5,p6
    fill(255,255,255)
    rect(0,0,800,800)
    fill(229,204,255)
    rect(10,10,550,300)
    rect(10,10,275,300)
    fill(255,204,255)
    triangle(255,310,315,310,285,280)
    triangle(255,10,315,10,285,40)
    fill(255,255,204)
    rect(10,ry,20,100)
    rect(540,ry2,20,100)
    fill(204,255,255)
    ellipse(bx,by,15,15)
    rect(10,p1,30,20)
    rect(50,p2,30,20)
    rect(90,p3,30,20)
    rect(520,p4,30,20)
    rect(480,p5,30,20)
    rect(440,p6,30,20)
    bx+=bxs
    by+=bys
    if keyPressed:
       if key == 'p':
           bxs=-2
           bys=2
       if key == 'w' and ry>=11:
           ry=ry-2
       if key == 's' and ry<209:
           ry=ry+2
       if key == 'o' and ry2>=11:
           ry2=ry2-2
       if key == 'l' and ry2<=209:
           ry2=ry2+2
    if bx<=-30 and b
        bxs=-bxs
    if bx>=rx2 and bx>=ry2 and by<=rx2-20 and by<=ry2+100:
         bxs=-bxs
    if bx<=19:
        bxs=0
        bys=0
        bx=285
        by=150
    if by<=18:
        bys=-bys
    if bx>=553:
        bxs=0
        bys=0
        bx=285
        by=150
    if by>=297:
        bys=-bys
    if bx<=19 and il==0:
         il+=1
         p1=800
    if bx<=19 and il==1:
         il+=1
         p2=800
    if bx<=19 and il==2:
        il+=1
        p3=800
    if by>=0 and ir==60:
        ir-=1
        p4=800
