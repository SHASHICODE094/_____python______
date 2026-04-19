import random

while True:
 choice= input("Enter your choice Y/N: ").lower()
 if (choice == "y"):
  dice1 = random.randint(1, 16)
#   dice2 = random.randint(1, 6)
  print(f'({dice1} {dice2})')
 elif(choice == "n"):
  print("thank you! you are not playing")
  break
 else:
    print("Invalid input")