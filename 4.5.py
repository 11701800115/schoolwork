from random import *
n=0
c=randint(0,100)  
while True:
    try:
        b=int(input("请输入0到100之间的整数："))
    except ValueError:
        print ("输入错误，请输入一个整数！")
        continue
    if b >c:
        print("遗憾，太大了。")
        n=n+1
        
    elif b<c:
        print("遗憾，太小了。")
        n=n+1
        
    else:
        n=n+1
        print("预测{}次，你猜中了。".format (n))
        break
