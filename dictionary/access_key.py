my_dict= {"car": "red", "train": "blue", "ship": "white", "plane": "green"}
# print(dict)

# car = dict["car"]
# print(car)

value= input("Enter the value to search").strip().lower()

if value in my_dict:
    print("key  exits.")
    print(value, ":", {my_dict[value]})
else:
    print("key 'not'exists. ")