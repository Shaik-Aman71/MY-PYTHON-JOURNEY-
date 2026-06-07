def fac(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
            
f=int(input("enter a number :"))
fac(f)
      