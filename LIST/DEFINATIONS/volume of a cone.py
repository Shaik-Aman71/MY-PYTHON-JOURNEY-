import math
def vol(n1,n2):
    v=1/3*3.14*math.pow(n1,2)*n2
    return v

a=int(input("R: "))
b=int(input("H: "))
x=vol(a,b)
print("volume of a cone :",x)