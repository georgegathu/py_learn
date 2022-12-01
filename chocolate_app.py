"""
    CHOCLATE DISTRIBUTION APP USING
    CONTROL FLOW STATEMENTS IN PYTHON:
    -if age > 20 then give 20 chocolates
    -if age > 10 and <= 20 then give 10 chocolates
    -if age > 5 and <= 10 then give 5 chocolates
    -if age < 5 then give no chocolate
"""
age = int (input("Please input your age: "))

if age > 20:
    print("Give 20 chocoaltes")
elif age > 10 and age <= 20:
    print("Give 10 chocoaltes")
elif age > 5 and age <= 10:
    print("Give 5 chocolates")
else:
    print("No Chocolate for you")