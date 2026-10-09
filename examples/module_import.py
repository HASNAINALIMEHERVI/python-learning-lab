"""Import a neighboring module without running its demonstration code."""
from recursion_examples import pattern

if __name__ == "__main__":
    print(pattern(3), end="")
