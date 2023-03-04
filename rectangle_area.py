# A program that prompts users for inputs to find the area and circumfrence of a rectangle 
width = float(input("Input Width: ")) 
height = float(input("Input Height: "))
area = width * height

print(f"The area of the rectangle is {area}")
circumference = 2 * (width + height)
print(f"The circumference is {circumference}")