import math
def iso(n1,n2):
    a=n2/4*(math.sqrt(4*math.pow(n1,2)-math.pow(n2,2)))
    return a

a=int(input("enter a number 1: "))
b=int(input("enter a number 2: "))
x=iso(a,b)
print("area of isosceles triangle is",x)
