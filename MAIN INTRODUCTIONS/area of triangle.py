import math
a=int(input("Enter the A value:"))
b=int(input("Enter the B value:"))
c=int(input("Enter the C value:"))
s=a+b+c/2
c=s*s-a*s-b*s-c
T=math.sqrt(c)
print("The area of the triangle is ",T)