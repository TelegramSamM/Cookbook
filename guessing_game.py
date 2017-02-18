import random

# Game Setup
print("Welcome to the guessing game.")
number_of_guesses = 3 # user has three guesses before losing game
user_won = False

# computer picks random number between 1-10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
    # user guesses number
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)

    # computer tells user whether guess was too high or too low
    if user_guess == correct_answer:
        print("Good guess!")
        print("You are correct!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Sorry, You guessed too high!")
    elif user_guess < correct_answer:
        print("Sorry, you guessed too low!")

    number_of_guesses -= 1

if user_won == True:
    print("You win!")
else:
    print("You lose!")
