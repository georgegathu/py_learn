secret_number = 10
guess_count = 0
guess_limit = 2

while guess_count < guess_limit:
    guess = int(input('Guess a number: '))
    guess_count += 1 
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed. Try again")
