value = int(input("Enter number in binary  or decimal.: "))
print("1. To convert binary.")
print("2.to  convert decimal")
choice=int(input("Enter your choice.: "))
if choice == 1:
    print("Decimal value = ", value)
    n=value
    result=0
    rem=""
    while n>0:
        rem= n%2
        result= f"{rem}{result}"
        n=n//2
       
    print(f"Binay value of {value} = {result}")
elif choice == 2:
    print("Binary value = ", value)
    value_str= str(value)
    result= int(value_str, 2)
    print(f"Decimal value of {value} = {result}")