"""Positive and negative step examples; stop is excluded."""
if __name__ == "__main__":
    text = "01234567"
    print(text[1:4:2])  # 13: indices 1 and 3
    print(text[4:1:-1])  # 432: a negative step walks backward
    print(text[-1:-4:-1])  # 765
