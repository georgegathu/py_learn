# A QUIZ GAME 

# Ask the user a bunch of quiz
# For every correct answer reward them with a point.

print("Welcome to my Quiz Game")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay, lets play :-)")
score = 0

answer = input("What does ICU stand for? ")
if answer.lower() == "intensive care unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the current President of Kenya ? ")
if answer.lower() == "william ruto":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who is the inventor of Linux? ")
if answer.lower() == "linus torvalds":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USA stand for? ")
if answer.lower() == "united states of america":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 40 + 45 equals to? ")
if answer.lower() == "95":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Java Script commonly used for? ")
if answer.lower() == "web development":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score / 6 * 100) + "%.")