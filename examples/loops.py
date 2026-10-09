"""Personal Python practice example; not a production application."""

def main():
    for i in range(1,100):
        print(i)
    for n in range(1,100,4):#(stEP,STOP,JUMP)
        print(n)
    l=[1,2,3,4,5,6,7]#for loop with list
    print(type(l))
    for i in (l):
        print(i)
    j=(1,2,3,4,5,6,7)#for loop with touple
    print(type(j))
    for k in (j):
        print(k)
    b="sunny"#for loop with string
    print(type(b))
    for i in (b):
        print(i)
        

if __name__ == "__main__":
    main()
