"""Recursive algorithms with explicit educational input limits."""

def validate(number: int):
    if isinstance(number, bool) or not isinstance(number, int) or not 0 <= number <= 100:
        raise ValueError("Use a whole number from 0 to 100 for this recursion demo.")

def factorial(number: int) -> int:
    validate(number)
    return 1 if number == 0 else number * factorial(number - 1)

def recursive_sum(number: int) -> int:
    validate(number)
    return 0 if number == 0 else number + recursive_sum(number - 1)

def pattern(number: int) -> str:
    validate(number)
    return "" if number == 0 else "*" * number + "\n" + pattern(number - 1)

if __name__ == "__main__":
    print(factorial(6))
    print(recursive_sum(5))
    print(pattern(3), end="")
