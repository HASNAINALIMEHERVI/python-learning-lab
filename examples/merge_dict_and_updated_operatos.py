"""Personal Python practice example; not a production application."""

def main():
    # Dictionaries banate hain
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    
    print("Original dict1:", dict1)
    print("Original dict2:", dict2)
    
    # ---------- Merge operator | ----------
    merged = dict1 | dict2
    print("\nMerge (dict1 | dict2):", merged)
    print("dict1 after merge:", dict1)  # unchanged
    
    # ---------- Update operator |= ----------
    dict1 |= dict2
    print("\nAfter update (dict1 |= dict2):", dict1)  # changed inplace

if __name__ == "__main__":
    main()
