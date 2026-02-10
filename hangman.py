import random

words = ["python", "java", "array", "stacks", "graph", "trees"]

word=random.choice(words)

guessed_letters=[]
attempts=6

while attempts>0:
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter+" "
        else:
            display+="_ "

    print(display)

    if "_" not in display:
        print("You won....!")
        break

    guess=input("Enter a letter:").lower()

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts-=1
        print("Wrong guess\nattempts left:",attempts)

else:
    print("You lost the game\nThe word is",word)