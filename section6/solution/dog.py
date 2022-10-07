class Dog():
    def __init__(self, name: str, good_dog: bool):
        self.name = name
        self.good_dog = good_dog
        self.treats = 0

    def bark(self):
        return "Woof!"

    def eat_treats(self, n):
        print(f"Eating {n} treats...")
        self.treats -= n
        return self.treats

    def get_treats(self, n):
        print(f"Finding {n} treats...")
        self.treats += n
        return self.treats

    def __str__(self):
        return f"{self.name} is {'' if self.good_dog else ' not '}a good dog and has {self.treats} treats."

doggy = Dog(
    name="Harper",
    good_dog=True
)

print(doggy)
print(doggy.bark())

# Getting some treats
doggy.get_treats(5)
doggy.get_treats(6)

# Eating some...
doggy.eat_treats(8)

print(doggy)