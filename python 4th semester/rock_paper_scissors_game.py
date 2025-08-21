import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while True:
        try:
            
            player_choice = int(input("Enter the number of your choice (1-3): "))
            if player_choice not in choices:
                print("Invalid choice! Please choose 1, 2, or 3.")
                continue


            computer_choice = random.randint(1, 3)
            print(f"Computer chose: {choices[computer_choice]}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == 1 and computer_choice == 3) or \
                 (player_choice == 2 and computer_choice == 1) or \
                 (player_choice == 3 and computer_choice == 2):
                print("You win!")
            else:
                print("You lose!")

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()