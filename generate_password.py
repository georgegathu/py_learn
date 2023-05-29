import random

def generate_password(length):
  """Generates a random password of the specified length."""
  letters = "abcdefghijklmnopqrstuvwxyz"
  numbers = "0123456789"
  symbols = "!@#$%^&*()-_=+{}[]:<>,.?;'\""
  
  password = "".join(random.choice(letters + numbers + symbols) for _ in range(length))
  return password

def main():
  """Generates and prints a random password."""
  length = int(input("Enter the length of the password: "))
  password = generate_password(length)
  print(f"Your password is: {password}")

if __name__ == "__main__":
  main()
