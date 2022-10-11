class Dog():
    def __init__(self, name: str, good_dog: bool = True, age: int = 0):
        """This function specifies how to create a new Dog object"""
        self.name = name
        self.good_dog = good_dog
        self.age = age

    def bark(self):
        print("Woof!")

    def celebrate_birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        """
        The __str__ method is built in to most existing python objects. It is called
        implicitly when an object is printed or included in an f-string!
        """
        return f"{self.name} is {'' if self.good_dog else ' not '}a good dog and is {self.age} years old."

doggy1 = Dog(
    name="Harper",
)

doggy2 = Dog(
    name="Quinn",
)

print(f"doggy1: {doggy1}")
print(f"doggy1: {doggy2}")
doggy1.bark()

# Aging up
doggy1.celebrate_birthday()

for i in range(11):
    doggy2.celebrate_birthday()

# Printing ages
print(f"doggy1's age is {doggy1.get_age()}")
print(f"doggy2's age is {doggy2.get_age()}")

# Printing dogs again
print(f"doggy1: {doggy1}")
print(f"doggy1: {doggy2}")