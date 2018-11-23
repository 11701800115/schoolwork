n=eval(input(""))
f=1

for i in range (2,n):
    
    if n%i==0 :
        f=0
if f==1:
    print("yes")
else:
    print("no")
