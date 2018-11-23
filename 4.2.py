z=0
s=0
k=0
q=0
a=input()
for i in a :
    if "A"<=i<="Z" or "a"<=i<"z":
        z=z+1
    elif "0"<=i<="9"  :
        s=s+1
    elif i==' ':
        k=k+1
    else:
        q=q+1
print("英文字符有{}个，数字有{}个，空格有{}个，字符有{}个.".format(z,s,k,q))
