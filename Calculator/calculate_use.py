import calculate
print("The Calculator ")
value1= int(input("Enter the 1st number : "))
value2= int(input("Enter the 2nd number : "))
print("__-----OPTION-----__")
print("1. Addition")
print("2. Subtractio")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter your choice! "))
if choice==1:
    calculate.addition(value1, value2)
elif choice==2:
    calculate.subtraction(value1, value2)
elif choice==3:
    calculate.multiplication(value1, value2)
elif choice==4:
    calculate.divission(value1, value2)




































