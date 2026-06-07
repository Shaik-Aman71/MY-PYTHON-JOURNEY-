a=int(input("give the year:"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("the given year is a leap year")
else:
    print("the given year is not a leap year")    