import jieba
txt=open("c:/Users/Administrator/Desktop/红楼梦.txt","r",encoding='GB18030').read()#开始
excludes={"什么","一个","我们","你们","如今","说道","知道","姑娘","起来"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="贾母" or word=="老太太":
        rword="贾老太婆"
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))


