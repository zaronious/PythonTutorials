class Person:
    def __init__(self, name):
        self.name = name

    # dunder is double underscore, repr is the representation of how calling the
    # Person class looks when it's returned
    # also called data model methods
    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid Argument, must be int")

        self.name = self.name * x

    def __call__(self, y):
        print("Called this function", y)

    def __len__(self):
        return len(self.name)


p = Person("Zaron")
print(p)
p * 4
print(p)
p(4)
print(len(p))
