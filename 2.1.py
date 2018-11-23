F=input("请输入温度体系符号：")
if F in ["F","f"]:
    t=eval(input("请输入温度值："))
    c=(t-32)/1.8
    print("转换后的温度是:{:.0f}C".format(c))
elif F in ["C","c"]:
    t=eval(input("请输入温度值："))
    f=(t*1.8)+32
    print("转换后的温度是:{:.0f}F".format(f))
else:
    print("输入符号错误")
    
