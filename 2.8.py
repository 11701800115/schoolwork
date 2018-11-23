from turtle import *
setup(600,600,200,200)
penup()
speed(1000)
fd(2)
pendown()
left(90)
def circle():
    global a
    a=a+2
    fd(a)
    left(90)
a=2
for i in range(107):
    
    circle()
