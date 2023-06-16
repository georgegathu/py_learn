height = int(input("What is your height in feet? "))
bill = 0

if height >= 2:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 10:
        bill = 250
        print("Ticket Price is 250")
    elif age <= 18:
        bill = 350
        print("Ticket Price is 350")
    else:
        bill = 600
        print("Ticket Price is Pay 600")

        want_photo = input("Do you want a photo(Y/N)? ")
        if want_photo == "Y" or want_photo == "y"
        bill = bill + 50

        print(f"Your total bill is{bill}")

else:
    print("Can't ride")
print("Bye bye!")