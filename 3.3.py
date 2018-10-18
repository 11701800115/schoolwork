dayup,dayfactor=1.0,0.01
for i in range(365):
     if i %7 in [4,5,6,7]:
        dayup=dayup*(1+dayfactor)
     else:
        dayup=dayup
     while i %10 in [0]:
       break
print("10天:{:.2f}.".format (dayup))
        
for i in range(365):
     if i %7 in [4,5,6,7]:
        dayup=dayup*(1+dayfactor)
     else:
        dayup=dayup
     while i %15 in [0]:
       break
print("15天:{:.2f}.".format (dayup))        
        
        
   
   
