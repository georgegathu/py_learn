# Functions
'''
official documentation:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''

# Ask for user's name
name = input("Whats your name? ")

# Remove whiespace from str
name = name.strip()

# Great the user
print(f"Hello, {name}")