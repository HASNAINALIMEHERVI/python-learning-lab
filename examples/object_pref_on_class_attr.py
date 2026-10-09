"""Personal Python practice example; not a production application."""

def main():
    class att:
        a=5
    
    o=att()
    print(o.a)
    o.a=0
    print(o.a)
    print(att.a)

if __name__ == "__main__":
    main()
