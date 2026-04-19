import random

random_Number = random.randint(1, 100)
while True:
   # print("random number : ", random_Number)
    choice =int(input("Guess the number : "))
    if random_Number == choice:
        print("Your no. is MATCH with random number")
        break
    elif random_Number < choice:
        print("You are guessing too HIGH")
    elif random_Number > choice:
        print("You are guessing too LOW")
    else:
        print("Invalid input")
        
