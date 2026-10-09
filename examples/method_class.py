"""Personal Python practice example; not a production application."""

def main():
    class num:
        a=4
        def show(self):
            print("the value of a=",self.a)
        @classmethod
        def slow(cls):#shows the class instance
            print("the value of a=",cls.a)
    o=num()
    o.a=45
    o.show()
    o.slow()

if __name__ == "__main__":
    main()
