class Vehicle:

    # class attribute
    species = "car"

    # instance attribute
    def __init__(self, name, color):
        self.name = name
        self.color = age

    def drive(self):
        return "{} is now moving".format(self.name)

# instantiate the Parrot class
audi = Vehicle("Audi", "black")
bmw = Vehicle("BMW", "blue")

# access the class attributes
print("BMW is a {}".format(blu.__class__.species))     # BMW is a car
print("Audi is a {}".format(woo.__class__.species))    # Audi is a car

# access the instance attributes
print("{} is {} in color".format( audi.name, audi.color)) # Audi is black in color
print("{} is {} in color".format( bmw.name, bmw.color))   # BMW is blue in color

print(bmw.dance()) # BMW is now moving
