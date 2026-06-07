def m(n1,n2,n3,n4,n5):
    sum=n1+n2+n3+n4+n5
    return(sum) 
def n(n1,n2,n3,n4,n5):
    avg=n1+n2+n3+n4+n5/5
    return(avg)
a=int(input("enter the marks for english :"))
b=int(input("enter the marks for maths :"))
c=int(input("enter the marks for science :"))
d=int(input("enter the marks for social :"))
e=int(input("enter the marks for telugu :"))
x=(m(a,b,c,d,e))
y=(n(a,b,c,d,e))
print("The total marks are :",x)
print("the total average is :",y)
z=y
if(z>=250):
    print("GRADE:A")
elif(z>200):
    print("GRADE:B")
elif(z>150):
    print("GRADE:C")
elif(z>100):
    print("GRADE:D")
else:
    print("GRADE:F")        