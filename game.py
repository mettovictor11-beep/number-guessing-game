
import random
username = input("Enter your username: ")

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
    exit()

attempts = 0
guessed_correctly = False
wrong_guesses = 0


while attempts < max_attempts and guessed_correctly == False:

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    attempts += 1

    if guess > secret_number:
        print("Too High!")
        wrong_guesses += 1

    elif guess < secret_number:
        print("Too Low!")
        wrong_guesses += 1

    else:
        print("Congratulations! You guessed correctly!")
        guessed_correctly = True

    if wrong_guesses == 3:
        if secret_number % 2 == 0:
            print("HINT: The secret number is EVEN.")
        else:
            print("HINT: The secret number is ODD.")

    if guessed_correctly == False:
        print("Remaining guesses:", max_attempts - attempts)


if guessed_correctly:
    print("\nYou won the game!")
    print("Total attempts used:", attempts)

else:
    print("\nGAME OVER!")
    print("You have run out of guesses.")
    print("The correct number was:", secret_number)


if guessed_correctly:
    result = "Won"
else:
    result = "Lost"

with open("scores.txt", "a") as file:
    file.write(
        f"{username},{difficulty},{attempts},{result}\n"
    )

print("Your score has been saved!")

