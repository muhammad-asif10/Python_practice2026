class Dog:
    def __init__(self, name, breed):
        self.name = name
        self._breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

    def describe(self):
        print(f"{self.name} is a {self._breed}.")

# Create instances of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

# Access attributes and call methods
print(my_dog.name)
my_dog.bark()
your_dog.describe()