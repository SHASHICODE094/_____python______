print('This is pattern application.')
n = int(input("Enter value to print pattern"))
starting_point= int(input("Enter the starting point"))
mid_point= int(input("Enter the mid point"))

print('1. "*" pattern')
print('2. "number" pattern')
choice = int(input("Enter your choice to print pattern"))
# range() arg 3 must not be zero
for i in range(starting_point, n, mid_point):
    for j in range(i+1):
        # print(i, end=" ")
          if choice==1:
            print("*", end=" ")
          elif choice==2:
            print(i, end=" ")
          else:
           print('Invalid')
    print()


  