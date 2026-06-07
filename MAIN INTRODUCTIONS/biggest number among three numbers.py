a = int(input("Enter number n1 : "))
b = int(input("Enter number n2 : "))
c = int(input("Enter number n3 : "))
if(a > b and a > c):
    print("Number 1 is biggest")
elif(b > a and b > c):
    print("Number 2 is biggest")
else:
    print("Number 3 is biggest")