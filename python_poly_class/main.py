from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.make_sound())

if __name__ == "__main__":
    main()
