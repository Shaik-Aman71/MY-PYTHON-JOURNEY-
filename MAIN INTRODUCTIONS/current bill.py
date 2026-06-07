pr=int(input("Enter the previous reading:"))
cr=int(input("Enter the current reading:"))
un=cr-pr
if(un>=2000)and(un<=3000):
    A=un*10
elif(un>=3000)and(un<=4000):
    A=un*20
elif(un>=4000)and(un<=5000):
    A=un*35
elif(un>=5000):
    A=un*40    
else:
    A=un*45            
print("the previous reading:",pr)
print("the current reading:",cr)
print("the units:",un)
print("the Amount:",A)