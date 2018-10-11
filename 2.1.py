#e1.1TempConvert.py
SymbolStr = input("请输入温度体系符号: ")
if SymbolStr in ['F', 'f']:
    t = eval(input("请输入温度值: "))
    C = (t - 32) / 1.8
    print("转换后的温度是:{:.0f}C".format(C))
elif SymbolStr in ['C', 'c']:
    t = eval(input("请输入温度值: "))
    F = t * 1.8 + 32
    print("转换后的温度是:{:.0f}F".format(F))
else:
    print("输入符号错误")
