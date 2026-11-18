
import random

secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")


print("\nChoose your difficulty:")
print("1. Easy - 10 attempts")
print("2. Medium - 7 attempts")
print("3. Hard - 5 attempts")

difficulty = input("Enter your choice (1/2/3): ")

if difficulty == "1":
    max_attempts = 10
    print("You selected Easy mode!")

elif difficulty == "2":
    max_attempts = 7
    print("You selected Medium mode!")

elif difficulty == "3":
    max_attempts = 5
    print("You selected Hard mode!")

else:
    print("Invalid choice! Please restart the game.")

attempts = 0
guessed_correctly = False


while attempts < max_attempts and guessed_correctly == False:

    guess = int(input("\nEnter your guess: "))

    attempts += 1

    if guess > secret_number:
        print("Too High!")

    elif guess < secret_number:
        print("Too Low!")

    else:
        print("Congratulations! You guessed correctly!")
        guessed_correctly = True

    remaining_guesses = max_attempts - attempts

    if guessed_correctly == False:
        print("Remaining guesses:", remaining_guesses)
