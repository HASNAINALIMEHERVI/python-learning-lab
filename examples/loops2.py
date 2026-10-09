"""Personal Python practice example; not a production application."""

def main():
    for i in range(1,4):   
     pass #iska matlb he k ye baad me dekhe ge yani kuch ni kro
    a=[1,3,5]
    for i in (a):
        print(i)
    else:
        print("done")
        for i in range (1,100):
            if(i>34):
             break
            print(i)
        for i in range (1,100):
            if(i==34):
             continue#sirf 34 ni likhe ga
            print(i)

if __name__ == "__main__":
    main()
