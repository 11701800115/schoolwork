import turtle as t
import datetime 
t.speed(10)
global hues
hues=0
t.color(1,0,0)
def drawcolor(hues):
    hues=hues*3.59
    
    rgb=[0.0,0.0,0.0]
    i=int(hues/60)%6
    f=hues/60-i
    if i==0:
        rgb[0]=1;rgb[1]=f;rgb[2]=0
    elif i==1:
        rgb[0]=1-f;rgb[1]=1;rgb[2]=0
    elif i==2:
        rgb[0]=0;rgb[1]=1;rgb[2]=f
    elif i==3:
        rgb[0]=0;rgb[1]=1-f;rgb[2]=1
    elif i==4:
        rgb[0]=f;rgb[1]=0;rgb[2]=1
    elif i==5:
        rgb[0]=1;rgb[1]=0;rgb[2]=1-f
    return rgb
def drawline(draw):
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def drawdigit(D):
    global hues
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [2,3,4,5,6,8,9] else drawline(False)
    hues=hues+3
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,1,3,4,5,6,7,8,9] else drawline(False)
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,2,3,5,6,8,9] else drawline(False)
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,2,6,8] else drawline(False)
    t.left(90)
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,4,5,6,8,9] else drawline(False)
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,2,3,5,6,7,8,9] else drawline(False)
    hues=hues+1
    rgb=drawcolor(hues)
    t.color(rgb[0],rgb[1],rgb[2])
    drawline(True) if D in [0,1,2,3,4,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawdate(date):
    for i in date:
        
        drawdigit(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawdate(datetime.datetime.now().strftime('%Y%m%d'))
    t.hideturtle()
main()
