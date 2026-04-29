lst = []

while True:
  try:
     print("you have a list and you have option to do with list")
     print("                                                                                    ")
     print("1.Add item in list \
       2.Add item at any place\
       3.Delete an item\
       4.Print the list")
     choice = int(input("Enter your choice: "))
     if choice<1 or choice>4: 
       print("Invalid input")
     elif choice == 1:
      item = input("Enter item: ")
      lst.append(item)
     elif choice == 2:
      item = input("Enter item: ")
      position = int(input("Enter position: "))
      lst.insert(position, item)
     elif choice == 3:
      item = input("Enter item to delete: ")
      lst.remove(item)
     elif choice == 4:
      print(lst)
     else:
      print("PROGRAMME EXIT-------")
      break
  except: 
    print("you have an error!")