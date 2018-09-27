import turtle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-100)
t.seth (-90)
t.fd(50*(3**(1/2)))
t.pendown()
t.seth(60)
for i in range (3):
    t.fd(200)
    t.right(120)
t.penup()
t.seth(0)
t.goto(0,0)
t.fd(-50)
t.pendown()
for i in range (3):
    t.fd(100)
    t.right(120)
