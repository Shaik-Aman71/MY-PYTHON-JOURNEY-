n=int(input("enter a number:"))
c=0
for i in range(1,n+1):
    if(n%i==0) and (n%n==0):
        c=c+1
        print(c)
if(c==2):
    print("it is a prime")
else:
    print("it is a composite")            
        