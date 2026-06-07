import math
def eq(n):
    a=(math.sqrt(3/4))*math.pow(n,2)
    return a

num=int(input("Enter a side value:"))
x=eq(num)
print("area of eqi-tri :",x)