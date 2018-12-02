fo=open("c:/score.csv","r+")#开始
fw=open("newscore.csv","w")
ls=[]
for line in fo:
    line=line.replace("\t",",")
    line =line.replace("\n","")
    ls.append(line.split(","))#到此为止把表格导入列表
maxgrade=[0,0,0,0]
mingrade=[0,100,100,100]
avg=[0,0,0,0]
total=['总分',0,0,0,0,0]
e=1
for i in ls[1:]:#表格除第一个列表
    for k in range(1,4):
        if maxgrade[k]<eval(i[k]):
            maxgrade[k]=eval(i[k])
        elif mingrade[k]>eval(i[k]):
            mingrade[k]=eval(i[k])#最大最小值的求出
        avg[k]=avg[k]+eval(i[k])#平均值
        total[e]=total[e]+eval(i[k])#总分
    e=e+1
for j in range(1,4):
    avg[j]=avg[j]/(len(ls)-1)#计算平均值    
for m in range(6):
    ls[m].append(str(total[m]))

for row in ls :
    print(row)
    fw.write(",".join(row)+"\n")
print(total)
print(avg)
print(maxgrade)
print(mingrade)
print(ls)
fw.close()
fo.close()
