print('This is pattern application.')

print('There are mainly two type of pattern, You need to choose')
print('1. Filled shape')
print('2. "Hollow shape')
choice_shape = int(input("Enter your choice to print pattern : "))
if choice_shape==1:
    print('Print filled shape')
    print('Please choice the side of shape print')
    print('1.Left')
    print('1.Mid')
    print('1.Right')
    choice_side = int(input('Enter your side : '))

    if choice_side==1:
        print('Print in Right side ')
        n = int(input("Enter value to print pattern :"))
        starting_point= int(input("Enter the starting point :"))
        mid_point= int(input("Enter the mid point : "))
 
        print('1. "*" pattern')
        print('2. "number" pattern')
        choice = int(input("Enter your choice to print pattern :"))
        # range() arg 3 must not be zero
        for i in range(starting_point, n, mid_point):
            for j in range(i+1, n, mid_point):
        #   print(i, end=" ")
              if choice==1:
                  print("*", end=" ")
              elif choice==2:
                  print(i, end=" ")
              else:
                  print('Invalid')
            print()

elif  choice_shape==2:
    print('Print Hollow shape')
else:
    print("Invalid input") 



  