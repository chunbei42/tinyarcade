import random

CHOICES = ["rock", "paper", "scissors"]

WINNING_MOVES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_computer_choice():
    return random.choice(CHOICES)


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if choice in CHOICES:
            return choice

        print("Invalid choice. Please enter rock, paper, or scissors.")


def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    if WINNING_MOVES[player_choice] == computer_choice:
        return "player"

    return "computer"


def play():
    player_score = 0
    computer_score = 0

    print("\n=== Rock, Paper, Scissors ===")
    print("First to 3 points wins!")

    while player_score < 3 and computer_score < 3:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(player_choice, computer_choice)

        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score — You: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("\nCongratulations! You won the match!")
    else:
        print("\nComputer won the match. Try again!")


if __name__ == "__main__":
    play()
