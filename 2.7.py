import turtle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-50*(3**(1/2)))
t.pendown()
t.seth(30)
for i in range (3):
    t.fd(150)
    t.right(120)
t.penup()
t.seth(0)
t.fd(100*(3**(1/2)))
t.seth(-150)
t.pendown()
for i in range (3):
    t.fd(150)
    t.right(120)
