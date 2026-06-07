n=int(input("enter the range of loop:"))
i=1
a=0
b=1
print(a) ; print(b)
while(i<=n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1