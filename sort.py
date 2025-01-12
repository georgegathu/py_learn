# Find th second largest number without using sort function in python
import heapq

numbers = [150, 250, 350, 450, 550]
result = heapq.nlargest(2, numbers)[1]
print(result)