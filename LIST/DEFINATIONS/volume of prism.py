import math
def pri(a,b):
    c=1/2*a*b
    d=(1/2)*math.pow(a,2)
    v=c*d
    return(v)

num1=int(input("BREADTH:"))
num2=int(input("HEIGHT:"))
x=pri(num1,num2)
print("volum of prism is :",x)