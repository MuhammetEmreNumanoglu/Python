import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def get_winner(player, computer):
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"

player_score = 0
computer_score = 0

print("Rock, Paper, Scissors! (type 'quit' to stop)")

while True:
    player = input("\nYour choice: ").lower().strip()
    if player == "quit":
        break
    if player not in CHOICES:
        print(f"Invalid. Choose from: {', '.join(CHOICES)}")
        continue

    computer = random.choice(CHOICES)
    print(f"Computer chose: {computer}")

    result = get_winner(player, computer)
    if result == "player":
        print("You win!")
        player_score += 1
    elif result == "computer":
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie!")

print(f"\nFinal: You {player_score} - {computer_score} Computer")
