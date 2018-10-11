import turtle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-100)
t.seth(90)
t.fd(-100)
for i in range(4):
  t.penup()
  t.fd(50)
  t.pendown()
  t.fd(100)
  t.penup()
  t.fd(50)
  t.right(90)
