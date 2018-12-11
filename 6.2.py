def repeatjudge(chlist:list):
    for i in chlist:
        if chlist.count(i)>1:
            return True
        else:
            return False
ls=['w','3','p','k']
if repeatjudge(ls):
    print('yes')
else:
    print('no')
