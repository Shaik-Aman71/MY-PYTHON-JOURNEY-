print("STAR PATTERN")
row=int(input("enter the number of rows:"))
for i in range(1,row+1,1):
    for j in range(1,i+1):
        j=("*")
        print(j,end=' ')
    print(" ")
for i in range(row,0,-1):
    for j in range(1,i,1):
        j=("*")
        print(j,end=' ')
    print(" ")
