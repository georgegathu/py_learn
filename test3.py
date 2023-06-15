# A PROGRAM TO CALCULATE WHETHER A YEAR IS LEAP YEAR OR NOT

year = float(input("Input year you want to cheeck: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")