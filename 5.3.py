def isNum(n):
    if type(n) is float:
        print("该字符是浮点数")
    elif type(n) is tuple:
        print("该字符是复数")
    elif type(n) is int:
        print("该字符是整数")
    else:
        print("请输入数字")
n=eval(input())
isNum(n)
        
    
