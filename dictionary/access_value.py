my_dict ={ 'car':'red', 'bird':'flying', 'bull':'run', 'taxi':'passenger'}
print(my_dict)

# value = my_dict['taxi']
keys = input("Enter the key").strip().lower()
value = my_dict[keys]
# print(f"key is {keys} and value is {value}" )
if keys in my_dict:
    print(f"Found the {keys}")
    print(f"value of {keys} is {value}")
else:
    print("Not found the keys")
