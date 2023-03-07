# Program to Print Odd Numbers from 1 to N using while loop in Python
 
num = int(input(" Please Enter the Maximum Value : "))
 
number = 1
 
while number <= num:
    if(number % 2 != 0):
        print("{0}".format(number))
    number = number + 1