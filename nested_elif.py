# Nested elif : is used when we have more than 2 condtions to make the program flow more readable
height = int(input("What is your height in feet? "))

if height >= 2:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 10:
        print("Pay ksh 250")
    elif age <= 18:
        print("Pay ksh 350")
    else:
        print("Pay 600")
else:
    print("Can't ride")
print("Bye bye!")