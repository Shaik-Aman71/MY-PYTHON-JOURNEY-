def cal1(num1,num2):
    sum=num1+num2
    return sum
def cal2(num1,num2):
    sub=num1-num2
    return sub
def cal3(num1,num2):
    pro=num1*num2
    return pro
def cal4(num1,num2):
    div=num1/num2
    return div
def cal5(num1,num2):
    fd=num1//num2
    return fd
def cal6(num1,num2):
    mod=num1%num2
    return mod
def cal7(num1,num2):
    pow=num1**num2
    return pow

a=int(input("enter the Num1:"))
b=int (input("enter the Num2:"))
x=cal1(a,b)
c=cal2(a,b)
v=cal3(a,b)
z=cal4(a,b)
n=cal5(a,b)
o=cal6(a,b)
p=cal7(a,b)
print("the sum of two numbers:",x)
print("the sub of two numbers:",c)
print("the product of two numbers:",v)
print("the division of two numbers:",z)
print("the floor division of two numbers:",n)
print("the mod of two numbers:",o)
print("the power of two numbers:",p)