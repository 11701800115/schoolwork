#e1.1TempConvert.py
TempStr = eval(input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F','f']:
               C= (TempSter-32)/1.8)
               print ("转换后的温度是{:.2f}C".format (C))
elif TempStr[-1] in ['c','C']:
               F=1.8*TempStr+32
               print("转换后的温度是{:.2f}F".format(F))
else:
               print("输入格式错误“）
