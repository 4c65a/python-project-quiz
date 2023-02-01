print("Welcome to a random trivia game")

print()

print("Answer with yes or not")

print()
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print()

print("Okay! Let's play :)")
score = 0

print()

answer = input("What does CPU stand for? ")

print()

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many stars does the US flag have?")
if answer.lower() == "50":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What day and month was the first atomic bomb dropped? ")
if answer.lower() == "August 6th":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
# Change score
print("You got " + str((score / 5) * 100) + "%.")
