print("You have an entrace test which is of total 100marks, You have attend it find your choice with marks achieve. THANK YOU!")
cuttoff =int(input("Enter marks : "))

if cuttoff >= 87:
    print ("You are eligible for BCA")
elif cuttoff >= 75:
    print ("You are eligible for BCS")
elif cuttoff >= 60:
    print ("You are eligible for BIT")
else :
    print("You are not qualified, please try gain or get in other subject")
