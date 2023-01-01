#CALCULATOR TO CALCULATE ALL THE BASIC ARITHMETICS

num_1 = float(input("Enter first number: "))
opp = input("Enter operator: ")
num_2 = float(input("Enter second number: "))

if opp == "+":
    print(num_1 + num_2)
elif opp == "-":
    print(num_1 - num_2)
elif opp == "/":
    print(num_1 / num_2)
elif opp == "*":
    print(num_1 * num_2)
else:
    print("Invalid operator")