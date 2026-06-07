def fib(n):
    i=1
    a=0
    b=1
    print(a) ; print(b)
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
        
z=int(input("enter a number :"))
x=fib(z)
print("the fibbanoci series is ",x)        