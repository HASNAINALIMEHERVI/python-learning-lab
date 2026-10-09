"""Arithmetic after numeric conversion, rather than string concatenation."""
import math

def main():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        if not all(math.isfinite(value) for value in (first, second)):
            raise ValueError("Numbers must be finite.")
    except ValueError:
        print("Enter finite numbers.")
        return
    print("First is greater:", first > second)
    print("Average:", first / 2 + second / 2)

if __name__ == "__main__":
    main()
