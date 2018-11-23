def isprime(n):
    
    for k in range(2,n):
        if n%k==0:
            return False
        return True
while True:
    try:
        n=int(input())
    except:
        print("输入错误，请输入整数。")
        continue
    if isprime(n):
        print("{}是质数。".format(n))
    else:
        print("{}不是质数。".format(n))
        

    
