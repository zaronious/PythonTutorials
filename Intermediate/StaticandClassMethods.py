class person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is", self.age, "years old")


newPerson = person("Zaron", 37)
print(person.getPopulation())
print(person.isAdult(5))

""" A class method is a method that’s shared among all objects.
To call a class method, put the class as the first argument.
Class methods can be can be called from instances and from the class itself.
All of these use the same method. The method can use the classes variables and methods.
Like a static method, a class method doesn’t need an object to be instantiated.

A class method differs from a static method in that a static method doesn’t know about the class itself.

In a classmethod, the parameter is always the class itself.

A static method knows nothing about the class or instance. You can just as well use a function call.
A static method doesn't need ANY input parameters

A class method gets the class when the method is called. It knows abouts the classes attributes and methods.
A class method NEEDS the class passed into it (cls)"""
