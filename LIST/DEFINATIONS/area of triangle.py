import math
def area(n1,n2,n3):
    s=(n1+n2+n3)/2
    x=s*(s-n1)*(s-n2)*(s-n3)
    q=math.sqrt(x)
    return q

a=int(input("enter a number 1: "))
b=int(input("enter a number 2: "))
c=int(input("enter a number 3: "))
x=area(a,b,c)
print("the area of triangle is ",x)
