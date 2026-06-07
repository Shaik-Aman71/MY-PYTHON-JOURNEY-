bs=int(input("enter the basic salary of the employee:"))
if(bs>=25000)and(bs<=35000):
    ta=bs*12/100
    da=bs*15/100
    hra=bs*22/100
    pf=bs*18/100
    it=bs*15/100
elif(bs>=35000)and(bs<=45000):
    ta=bs*15/100
    da=bs*18/100
    hra=bs*20/100
    pf=bs*20/100
    it=bs*18/100
elif(bs>=45000):
    ta=bs*18/100
    da=bs*20/100
    hra=bs*15/100
    pf=bs*22/100
    it=bs*19/100
else:
    ta=bs*20/100
    da=bs*15/100
    hra=bs*18/100
    pf=bs*19/100
    it=bs*16/100
gs=bs+ta+da+hra
dd=pf+it
ns=gs-dd
print("the basic salary:",bs)
print("the travel allowance:",ta)
print("the dearness allocance:",da)
print("the houserent allowance:",hra)
print("the provident fund:",pf)
print("the income tax:",it)
print("the gross salary:",gs)
print("the deductions:",dd)
print("the net salary:",ns)