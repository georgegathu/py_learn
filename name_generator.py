#  == 100 DAY CHALLENGE OF CODE( Day 1) == 

# 1. Create a greeting prompt for users
# 2. Ask the user for the city that your born in
# 3. Prompt the user to input the name of a pet
# 4. Combine their city name and pet name & show them their Group Name
# 5. Make sure the input cursor shows on a new line

print("Welcome to the Group Name generator!")
city = input("Which city are you born in? \n")
pet = input("What is your Pet name? \n")
group_name = city + " " + pet 
print("Your group name is " + group_name)
