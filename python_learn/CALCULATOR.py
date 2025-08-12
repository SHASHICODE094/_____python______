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
  print(f"The squareroot of {num} is : { m.sqrt(num)}")

elif choice =="3":
  print("Please select the  given shapes currently only first two are available")
  print("1.Circle ")
  print("2.Square ")   
  print("3.Rectangle ")
  print("4.Cylinder ")
  print("5.Cone ")
  choice = input("Enter your choice(like square) : ")

  if choice == "square":
   print(f"You have enter {choice} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to enter the SIDE of {choice} to calculate Area  ")
    side = int(input("Enter SIDE : "))
    #num2 = int(input("Enter breadth: ")) 
    print(f"The area of square is : {side}")
   elif calculate == "2":
    print(f"Now You have to enter the SIDE of {choice} to calculate Perimeter ")
    side = int(input("Enter lenght : "))
    print(f"The area of square is{4*side}")
 
  elif choice == "circle":
   print(f"You have enter {choice} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to enter the radius to calculate Area of {choice} ")
    r = int(input("Enter radius : "))
    print(f"The area of circle is : {3.14*r*r}")
   elif calculate == "2":
    print(f"Now You have to enter the radius to calculate Perimeter of {choice} ")
    r = int(input("Enter radius : "))
    print(f"The area of {choice} is{2*3.14*r}")

  elif choice == "rectangle":
   print(f"You have enter {choice} so next you select what do you want to calculate : ")
   print("1.Area ")
   print("2.Perimeter ")
   calculate = input("Enter your choice(like 1) : ")
   if calculate == "1":
    print(f"Now You have to enter the lenght and breadth to calculate Area of {choice} ")
    num1 = int(input("Enter lenght : "))
    num2 = int(input("Enter breadth: ")) 
    print(f"The area of {choice} is : {num1*num2}")
   elif calculate == "2":
    print(f"Now You have to enter the lenght and breadth to calculate Perimeter of {choice} ")
    num1 = int(input("Enter lenght : "))
    num2 = int(input("Enter breadth: ")) 
    print(f"The area of {choice} is{2*(num1+num2)}")  
   

else:
 print("Please check Input value!")