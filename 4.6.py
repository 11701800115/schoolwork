from random import *
a=["car","sheep","sheep"]
n=100000
b=0
c=0
for i in range(n):
    if choice(a)=="car":
        b=b+1
    else:
        c=c+1
print("坚持获胜次数：{}，改变获胜的次数：{}".format(b/n,c/n))
        
