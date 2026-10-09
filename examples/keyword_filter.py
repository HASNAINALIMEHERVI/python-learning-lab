"""A keyword exercise, not a reliable spam-detection system."""
KEYWORDS = ("buy now", "make money", "buy this")

def has_keyword(text: str) -> bool:
    return any(word in text.casefold() for word in KEYWORDS)

if __name__ == "__main__":
    text = input("Enter sample text: ")
    print("Keyword matched" if has_keyword(text) else "No keyword matched")
    print("This simple rule can produce false positives and false negatives.")
