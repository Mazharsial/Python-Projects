import random

# List of colors
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink']

# Randomly select a color
selected_color = random.choice(colors)

# Give the player 3 chances to guess the color
print("Welcome to 'Guess the Color!'")
print("I have selected a color. Try to guess it!")
print("You have 3 chances!")

# Loop for 3 attempts
attempts = 3
while attempts > 0:
    guess = input(f"You have {attempts} chances left. Enter your guess: ").lower()

    if guess == selected_color:
        print("Congratulations! You guessed it right!")
        break
    else:
        attempts -= 1
        print("Wrong guess! Try again.")

if attempts == 0:
    print(f"Sorry, you've run out of guesses. The correct color was {selected_color}.")