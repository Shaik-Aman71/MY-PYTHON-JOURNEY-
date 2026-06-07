import math
x1=int(input("enter the value of x1 :"))
x2=int(input("enter the value of x2 :"))
y1=int(input("enter the value of y1 :"))
y2=int(input("enter the value of y2 :"))
a=math.pow(x2-x1,2)
b=math.pow(y2-y1,2)
c=math.sqrt(a+b)
print("THE DISTANCE BETWEEN THE",(x1,y1),"AND",(x2,y2),":",c)