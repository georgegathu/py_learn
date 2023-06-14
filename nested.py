"""
1. Nested If: this is if inside if 
    syntax:
    if condition 1:
        statement 1
        if condition 2:
            statement 2
2. Nested if else: 
    syntax:
    if condition 1:
        statement 1
        if condition 2:
            statement 2
        else:
            statement 3
"""
# Example 1 (nested if else)
height = int(input("What is your height in feet? "))

if height > 1:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Pay ksh 300")
    else:
        print("Pay ksh 600")