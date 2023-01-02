# A PROGRAM TO CHECK NAME LENGTH 
#NAME MUST HAVE ATLEAST 3 CHARACTERS 
#NAME SHOULD NOT BE MORE THAN 50 CHARACTER
#OTHERWISE PRINT "NAME LOOKS GOOD!"

user_name = str(input("Enter your name: "))

if len((user_name)) < 3:
    print("Name is too short!")
elif len((user_name)) > 50:
    print("Name is too long!")
else:
    print("Name looks good!")