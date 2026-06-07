import math
def cal1(n1,n2,n3):
    math.pow(n2,2)-4*n1*n3
    print("Root 1:",(-n2+math.sqrt(d)/(2*n1)))
    print("Root 2:",(-n2-math.sqrt(d)/(2*n1)))
def cal2(n1,n2,n3):
    d=math.pow(n2,2)-4*n1*n3
    e=(-n2+math.sqrt(d))/(2*n1)
    f=(-n2-math.sqrt(d))/(2*n1)
    print("Root 1:",e)
    print("Root 2:",f)
def cal3(n1,n2,n3):
    d=math.pow(n2,2)-4*n1*n3
    g=-n2/(2*n1)
    h=math.sqrt(-d)/(2*n1)
    print("Root 1:",g,"+i",h)
    print("Root 2:",g,"-i",h)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=math.pow(b,2)-4*a*c
if d==0:
    print("Roots are real and equal")
    cal1(a,b,c)
elif d>0:
    print("Roots are real and unequal")
    cal2(a,b,c)
else:
    print("Roots are imaginary")
    cal3(a,b,c)