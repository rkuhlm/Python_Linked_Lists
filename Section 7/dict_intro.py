vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get('er5')
print(learner)
print()

# I can either index or use .get to retrieve the info at each key.
# .get will return none if the key does not exist
# indexing is faster though


vehicles["starfighter"] = "Lockheed F-104"
# this is how we add item into a Dic.
# starfighter is the key/index and lockheed f-104 is the value at the key/index
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# this is how we change values
vehicles["virago"] = "Yamaha XV535"


for key in vehicles:
    print(key, vehicles.get(key))

print()

for key, val in vehicles.items():
    print(key, val, sep=", ")

print()

# the .items is more time efficient for big data sets

# This is remove items from the Dic
# .pop will remove items and if we add "None" then the program will not crash if that item does not exist.
del vehicles["starfighter"]
vehicles.pop("toy")
vehicles.pop("f1", None)

for key, val in vehicles.items():
    print(key, val, sep=", ")