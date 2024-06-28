print("------CALCULATOR------")

num1=float(input("Enter Num1:"))
num2=float(input("Enter num2:"))

print("Press 1 for adittion")
print("Press 1 for subtraction")
print("Press 1 for multiplication")
print("Press 1 for division")

choice=int(input("Enter choice from 1-4:"))

if choice==1:
    print (num1 + num2)
elif choice==2:
    print (num1 - num2)
elif choice==3:
    print (num1 * num2)
elif choice==4:
    print (num1 / num2)
else:
    print("Invalid Input")



