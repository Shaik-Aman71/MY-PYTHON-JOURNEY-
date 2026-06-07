def cal(num):
    if(num%2==0):
        return "Even"
    else:
        return "odd"
    
n=int(input("enter a number :"))
x=cal(n)
print("the number is ",x)    