import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_player_choice():
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        player_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return player_choice

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Let's play Rock Paper Scissors!")

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    print(get_winner(player_choice, computer_choice))

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Thanks for playing!")