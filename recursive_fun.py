"""
Quiz:
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
NB:A recursive function is a function that calls itself again and again.
"""
def addition(number):
    if number:
        # call same function by reducing number by 1
        return number + addition(number - 1)
    else:
        return 0

res = addition(10)
print(res)