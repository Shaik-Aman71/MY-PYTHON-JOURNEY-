import math
P=int(input("principal amount: "))
R=int(input("Rate of interest: "))
N=int(input("Number of Periods: "))
S=1+R/100
C=P*math.pow(S,N)
print("Compound Interest is: ",C)