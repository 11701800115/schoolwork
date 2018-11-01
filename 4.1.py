
b=eval(input())
n=0

    
while True:
    b=eval(input("请输入0到9之间的整数："))
    if b >6:
        print("遗憾，太大了。")
        n=n+1
        
    elif b<6:
        print("遗憾，太小了。")
        n=n+1
        
    else:
        n=n+1
        print("预测{}次，你猜中了。".format (n))
        break
       
