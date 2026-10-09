"""A command-line number guessing practice game."""
import random

def feedback(guess: int, secret: int) -> str:
    if not 1 <= guess <= 100:
        raise ValueError("Enter a number from 1 to 100.")
    return "Too low" if guess < secret else "Too high" if guess > secret else "Correct"

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess a whole number from 1 to 100. Enter q to quit.")
    while True:
        try:
            value = input("Your guess: ").strip()
            if value.lower() == "q":
                return
            guess = int(value)
            result = feedback(guess, secret)
        except ValueError as exc:
            print(str(exc) if value.lstrip("-").isdigit() else "Enter a whole number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended.")
            return
        attempts += 1
        print(result)
        if guess == secret:
            print(f"You won in {attempts} attempts.")
            return

if __name__ == "__main__":
    main()
