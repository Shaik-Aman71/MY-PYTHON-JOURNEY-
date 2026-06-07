A=int(input("English marks: "))
B=int(input("Maths marks: "))
C=int(input("Science marks: "))
D=int(input("Social marks: "))
E=int(input("Computer Science marks: "))
Total=A+B+C+D+E
Average=Total/5
print("Total marks: ",Total)
print("Average marks: ",Average)
if(Average>90):
    print("Grade::A+")
else:
    print("Grade::A-")    
    
          