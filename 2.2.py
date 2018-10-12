TempStr = input("请输入带有符号的金额: ")
if  TempStr[-1] in ["$"]:
    C= eval(TempStr[0:-1])*6
    print ("转换后的金额是{:.2f}￥".format (C))
elif TempStr[-1] in ["￥"]:
     F=eval(TempStr[0:-1])/6
     print("转换后的金额是{:.2f}$".format(F))
else:
     print("输入格式错误")
