"""Correct prime testing; practice with loops and input validation."""
from math import isqrt

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, isqrt(number) + 1))

def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Enter a whole number.")
        return
    print("Prime" if is_prime(number) else "Not prime")

if __name__ == "__main__":
    main()
