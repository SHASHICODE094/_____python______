"""def greeting():
    return "Hi"
response=greeting()
print(response)
"""
import math as m
print("Lets calculate somethings")
print("Choose the option and enter input to see the results")
print("1.Simple calculator ")
print("2.Square calculator ")
print("3.Find area calculator ")
choice = input("Enter the operator (1, 2, 3): ")
if choice =="1": 
  print("Input two number and check the result!")
  num1 = int(input("Enter First number : "))
  num2 = int(input("Enter second number: "))
  operater = input("Enter the operator (+, -, *, /)")
  if operater == '+':
   print(f"Sum of {num1} and {num2} :", num1+ num2)
  elif operater == '-':
   print(f"Sub of {num1} and {num2} :", num1- num2)
  elif operater == '*':
   print(f"Multiple of {num1} and {num2} :", num1* num2)
  elif operater == '/':
   print(f"Division of {num1} and {num2} :", num1/ num2)
  else:
   print("Invalid Input")

elif choice =="2":
  num = int(input("Enter the number to find the squareroot  : "))
  print(f"The squareroot of given number is : { m.sqrt(num)}")

elif choice =="3":
  print("Please select the  given shapes currently only first two are available")
  print("1.Circle ")
  print("2.Square ")   
  print("3.Rectangle ")
  print("4.Cylinder ")
  print("5.Cone ")
  select = input("Enter your choice(like square) : ")

  if select == "square":
   print(f"You have Enter {select} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to Enter the two numbers to calculate Area of {select} ")
    num1 = int(input("Enter lenght : "))
    num2 = int(input("Enter breadth: ")) 
    print(f"The area of circle is : {num1*num2}")
   elif calculate == "2":
    print(f"Now You have to Enter the two numbers to calculate Perimeter of {select} ")
    num = int(input("Enter lenght : "))
    print(f"The area of circle is{4*num}")
 
  elif select == "circle":
   print(f"You have Enter {select} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to Enter the two numbers to calculate Area of {select} ")
    r = int(input("Enter radius : "))
    print(f"The area of circle is : {3.14*r*r}")
   elif calculate == "2":
    print(f"Now You have to Enter the two numbers to calculate Perimeter of {select} ")
    r = int(input("Enter radius : "))
    print(f"The area of circle is{2*3.14*r}")

if select == "rectangle":
   print(f"You have Enter {select} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to Enter the two numbers to calculate Area of {select} ")
    num1 = int(input("Enter lenght : "))
    num2 = int(input("Enter breadth: ")) 
    print(f"The area of circle is : {num1*num2}")
   elif calculate == "2":
    print(f"Now You have to Enter the two numbers to calculate Perimeter of {select} ")
    num1 = int(input("Enter lenght : "))
    num2 = int(input("Enter breadth: ")) 
    print(f"The area of circle is{2*(num1+num2)}")  
   

else:
 print("Please check Input value!")