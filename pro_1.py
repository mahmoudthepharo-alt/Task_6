class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name}")

dog_name = input("Enter the dog's name: ")
dog_breed = input("Enter the dog's breed: ")
my_dog = Dog(dog_name, dog_breed)
my_dog.bark()