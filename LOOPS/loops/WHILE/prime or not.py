n=int(input("enter the number:"))
i=1
c=0
while(i<=n):
    if(n%i==0) and(n%n==0):
        print(i) 
        c=c+1
    i=i+1      
if (c==2):
    print("Prime")
else:
    print("Not Prime")
    
