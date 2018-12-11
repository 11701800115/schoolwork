from random import random
def printintro():
    print("这个程序模拟两个选手A和B的兵乓球比赛")
    print("这个程序运行需要A和B的能力值（以0到1之间的小数表示）")
def getinputs():
    a=eval(input("请输入选手A的能力值（0-1）;"))
    b=eval(input("请输入选手B的能力值（0-1）:"))
    n=eval(input("模拟比赛的场次:"))
    return a,b,n
def simngames(n,probA,probB):
    winA,winB=0,0
    for i in range(n):
        scoreA,scoreB=simgame(3,probA,probB)
        if scoreA>scoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB
def simgame(n,probA,probB):#一局比赛要进行n场
    sa,sb=0,0
    for i in range(n):
        scoreA,scoreB=simgame(probA,probB)
        if scoreA > scoreB:
            sa+=1
            if sa == n//2+1:
                return sa,sb
        else:
            sb+=1
            if sb ==n//2+1:
                return sa, sb
def gameover2(a,b):
    if a==21 and b<20:
        return True
    elif a<20 and b==21:
        return True
    elif 21<a<30 and 21<b<30 and abs(a-b)==2:
        return True
    elif a==30 or b==30:
        return True
    return False
def gameover1(a,b):
    if a==11 and b<10:
        return True
    elif a<10 and b==11:
        return True
    elif 11<a<30 and 11<b<30 and abs(a-b)==2:
        return True
    elif a==30 or b==30:
        return True
    return False
def gameover(a,b):
    return a==30 or b==30
def simonegame(probA,probB):
    scoreA,scoreB=0,0
    serving=0
    t=0
    while not gameover2(scoreA,scoreB):
        if serving==0:
            if random() < probA:
                scoreA+=1
            else:
                scoreB+=1               
        else:
            if random() < probB:
                scoreB+=1
            else:
                scoreA+=1
        t=t+1
        if t%2==0:#t%5==0
            serving=(serving+1)%2
    return scoreA,scoreB
def printsummary(winA,winB):
    n=winA+winB
    print("竞技分析开始，共模拟{}场比赛".format (n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winA,winA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winB, winB/n))
def main():
    printintro()
    probA, probB, n = getinputs()
    winA, winB = simngames(n, probA, probB)
    printsummary(winA, winB)
main()

