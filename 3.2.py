dayup,dayfactor=1.0,0.01
for i in range(365):
    if i %7 in [1,2,3]:
        dayup=dayup
    else:
        dayup=dayup*(1+dayfactor)
print("能力有限每天努力的力量:{:.2f}.".format (dayup))
