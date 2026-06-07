def p(num):
    c=0
    for i in range(1,num+1):
        if(num%i==0) and (num%num==0):
             c=c+1
             print(c)
    if(c==2):
        return "prime"
    else:
        return "not prime"
n=int(input("enter a number :"))
x=p(n)     
print("the number is ",x)   

