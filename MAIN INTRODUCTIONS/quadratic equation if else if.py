import math
a=int(input("Enter the A value:"))
b=int(input("Enter the B value:"))
c=int(input("Enter the C value:"))
d=math.pow(b,2)-4*a*c
e=-b+d/2*a
f=-b-d/2*a
if(d==0):
    print("roots are real and equal")
    print("R1:",e)
    print("R2:",f)
elif(d>0):
    print("root are real and unequal",e,f)
    print("R1:",e)
    print("R2:",f)
elif(d<0):    
    p=-b/2*a
    q="i"*math.sqrt(d)/2*a
    print("the root are real and imaginary")
    print("R1:",p,"+i",q)
    print("R2:",p,"-i",q)
else:
    print("invalid")    