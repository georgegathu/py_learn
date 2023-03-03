# PYTHON LISTS
"""
        They are sequenced data types.
        An empty list is created using list() function
        Lists are mutable, i.e, they can be altered once declared
"""
#Declaring a List
S = ['Start', 22, 'Leave', 11+11]
S.append('My G')
print (S)
#Delete Third element in a List
S.pop(2)
print(S)
#Display the 4th element in a List
print(S[3])

#TUPLES IN PYTHON
"""
    Tuple - Is a sequence of immutable Python objects.
    They are just like Lists only that tuples cannot be changed once declared.
    They are usually faster than Lists
"""
tup = (1, 'One', 2, 'Two')
print(tup[3])


#ITERATIONS IN PYTHON
"""
    Also known as Looping
    Can be performed by 'for' and 'while' loops
    Apart from iterating upon a particular condition,
    we can also iterate on strings, lists and tuples.
"""
#Iteration by While Loop for a condition
x = 1
while (x < 5):
    print(x)
    x +=1
#Iteration by For Loop on the string
y = "Live Life"
for x in y:
    print(x)
#Iteration by loop on List
X = [1, 5, 10, 15, 20, 25]
for i in X:
    print(i)
#Iteration by For Loop for range
for x in range(0,5):
    print(x) 