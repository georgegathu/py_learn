# This program prints the even numbers from 1 to 100.

even_numbers = []

for i in range(1, 101):
  if i % 2 == 0:
    even_numbers.append(i)

for number in even_numbers:
  print(number)
