# This program says hallo to a user and asks for their names

print('Hello, whats your name? ')
myName = input()

print("Pleasure meeting you, " + myName)
print("The lenght of your name is: ")
print(len(myName))

print("How old are you? ")
myAge = input()
print("You will be " + str(int(myAge) + 1)  + ' in a year')
