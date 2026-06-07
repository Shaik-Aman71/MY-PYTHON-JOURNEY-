print("CONTINEOUS NUMBER")
row=int(input("enter the number of rows :"))
c=1
for i in range(1,row+1):
    for j in range(i):
        print(c,end=' ')
        c+=1
    print(" ")
    