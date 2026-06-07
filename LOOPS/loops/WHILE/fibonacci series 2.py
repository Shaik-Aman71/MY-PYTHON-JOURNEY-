n=int(input("how many terms? :"))
n1=0
n2=1
c=0
if(n<=0):
    print("please enter a positive integer:")
elif(n==1):
    print("fibanocci sequence upto",n,":")
    print(n1)
else:
    print("fibanocci sequence upto",n,":")
    while(c<n):
        print(n1,end='')
        next=n1+n2
        n1=n2
        n2=next
        c+=1  