"""Personal educational example."""

def main():
    a=set()
    b={1,2,2,3,4,3,5,6,7,6,"sunny"}
    c={1,2,4,6,7}
    print(b)
    b.add(566)
    print(b)
    print(b)
    print(b.union(c))
    print(b.intersection(c))
    

if __name__ == "__main__":
    main()
