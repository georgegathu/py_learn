def calculate_discount(amount, discount_rate):
  """
  Calculates the discount for a given amount and discount rate.

  Args:
    amount: The amount of money spent.
    discount_rate: The discount rate as a percentage.

  Returns:
    The amount of money saved.
  """

  discount = amount * discount_rate / 100
  return discount

def main():
  """
  Gets the amount spent from the user and calculates the discount.

  Prints the amount of money saved.
  """

  amount = float(input("Enter the amount spent: "))
  discount_rate = float(input("Enter the discount rate: "))

  discount = calculate_discount(amount, discount_rate)

  print("You saved $" + str(discount) + " on your purchase.")

if __name__ == "__main__":
  main()
