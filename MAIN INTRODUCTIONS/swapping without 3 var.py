a=int(input("Enter number n1:"))
b=int(input("Enter number n2:"))
print("Before swapping",a,b)
a+=-b
print("After swapping",a)
b+=a-b
print("After swapping",b)