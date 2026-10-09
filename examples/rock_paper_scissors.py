"""A single-round terminal learning game."""
import random
CHOICES = ("rock", "paper", "scissors")

def outcome(player: str, computer: str) -> str:
    if player not in CHOICES or computer not in CHOICES:
        raise ValueError("Choose rock, paper or scissors.")
    if player == computer:
        return "Draw"
    return "Win" if (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")) else "Lose"

def main():
    player = input("Rock, paper or scissors: ").strip().lower()
    if player not in CHOICES:
        print("Choose rock, paper or scissors.")
        return
    computer = random.choice(CHOICES)
    print("Computer:", computer)
    print(outcome(player, computer))

if __name__ == "__main__":
    main()
