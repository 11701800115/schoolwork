def rj(chilst:list):
    newset=set(chilst)
    if len(chilst)==len(newset):
        return False
    else:
        return True
ls=[1,2,3,4,5,'w',]
if rj(ls):
    print("yes")
else:
    print("no")
