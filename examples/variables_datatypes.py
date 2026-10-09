"""Personal educational example."""

def main():
    b=5==5
    print(b)
    c=8==9
    print(c)
    
    print("A\tB\tA or B")
    print("-" * 20)
    
    values = [True, False]
    
    for A in values:
        for B in values:
            print(f"{A}\t{B}\t{A or B}")
    
    
    print("A\tB\tA and B")
    print("-" * 20)
    
    values = [True, False]
    
    for A in values:
        for B in values:
            print(f"{A}\t{B}\t{A and B}")
    
    
            
    
    print("A\tnot A")
    print("-" * 15)
    
    values = [True, False]
    
    for A in values:
        print(f"{A}\t{not A}")

if __name__ == "__main__":
    main()
