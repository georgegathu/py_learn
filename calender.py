# Python program to display calendar of given month and the rest of the year

# import module
import calendar

year = int (input("Please input year: "))
month = int (input("Please input month: "))

# display the calendar month and the rest of the year
print(calendar.month(year, month))
print(calendar.calendar(year))