import math

def calculate_area(radius):
  """Calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """

  area = math.pi * radius ** 2
  return area

if __name__ == "__main__":
  radius = 5
  area = calculate_area(radius)
  print("The area of the circle is", area)

