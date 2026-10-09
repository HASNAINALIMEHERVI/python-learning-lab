"""Personal Python practice example; not a production application."""

def main():
    l={1,2,3,4,5}
    square=lambda x:x**2
    
    squared=(map(square,l))
    print(list(squared))
    # filter
    def func(n):
        if(n%2==0):
            return True
        return False
    even=list(filter(func,l))
    print(even)
    # reduce
    from functools import reduce
    product=reduce(lambda x,y:x*y,l)
    print(product)
    
        

if __name__ == "__main__":
    main()
