class Dog:
    species = "Mammal"

    def __init__(self, breed, name, spots, age):
        self.breed = breed
        self.name = name
        self.spots = spots
        self.age = age

    def bark(self, num):
        print("Woof my name is {}".format(self.name))
        print("You gave me the number ", num)


mydog = Dog(breed="Huskies", name="Sammy", spots=True, age=5)
print(mydog.breed)
print(mydog.name)
print(mydog.spots)
print(mydog.age)
print(mydog.species)
mydog.bark(67)


