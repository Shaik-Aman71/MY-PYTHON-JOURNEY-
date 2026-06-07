import math
a=int(input("Enter the A value:"))
b=int(input("Enter the B value:"))
c=int(input("Enter the C value:"))
D=math.pow(b,2)-4*a*c
R=-b+math.sqrt(D)/2*a
print("the root of quadratic equation",R)