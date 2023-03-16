# User interaction App
"""
print("Hello friend")
print("What is your name?") #Ask for friends name

my_name = input()

print("It is good to meet you " + my_name)
print("The length of your name is: ")
print(len(my_name))
print("What is your age?") # Ask for their age
my_age = input()
print("You will be " + str(int(my_age)+1) + " in a year")
"""

# Shortened version of the code above using concatination and type conversion
# from 9 lines of code to 4 lines of code
my_name = input("Hello friend \n" + "What is your name?\n ")
print("It is good to meet you "+ my_name + ", Your name length is " + (str(len(my_name))))
my_age = input("What is your age?\n ")
print("You will be "+ str(int(my_age)+1) + " in a year's time")
