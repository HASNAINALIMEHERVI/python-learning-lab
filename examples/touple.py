"""Personal educational example."""

def main():
    a=(1,2,"demo",4,)
    print(a)
    b=(2,)
    print(type(b))
    c=(1,2,3,4)
    print(c.count(3))
    print(c.index(3))
    print(len(c))
    print(sum(c))
    print(max(c))
    print(min(c))

if __name__ == "__main__":
    main()
