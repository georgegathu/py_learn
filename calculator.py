#Simple Basic Calculator
def sum (a,b): # Does the sumation
    return a+b

def sub (a,b): # Does the substruction
    return a-b

def multiply (a,b): #Does the multiplication
    return a*b

def divide (a,b): # Does the division
    return a/b 

a = float(input("Input first Number: "))
b = float(input("Input second Number: "))

option = int(input("""
Choose one of the options below: 
1.Add
2.Subtract 
3.Multiply 
4.Divide
5.Exit
"""))

while option !=5:
    if option ==1:
        print(sum(a,b))
        a = float(input("Input first Number: "))
        b = float(input("Input second Number: "))

        option = int(input("""
        Choose one of the options below:
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Exit
        """))

    elif option ==2:
        print(sub(a,b))
        a = float(input("Input first Number: "))
        b = float(input("Input second Number: "))

        option = int(input("""
        Choose one of the options below:
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Exit
        """))

    elif option ==3:
        print(multiply(a,b))
        a = float(input("Input first Number: "))
        b = float(input("Input second Number: "))

        option = int(input("""
        Choose one of the options below:
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Exit
        """))

    elif option ==4:
        print(divide(a,b))
        a = float(input("Input first Number: "))
        b = float(input("Input second Number: "))

        option = int(input("""
        Choose one of the options below:
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        5.Exit
        """))