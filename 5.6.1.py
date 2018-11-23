def fact(n):
    if n in [1,2]:
        return 1
    else:
        return fact(n-1)+fact(n-2)
n=eval(input())
print(fact(n))
