# Define a class with variables for name and country.
# Then define a method that belongs to the class. 
# The method prints a sentence that uses these variables.

class Location:
    # Constructor (__init__) to initialize name and country attributes
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # Method to print location details
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the Location class
loc1 = Location("Joshua Therence Templo", "Cebu City")
loc1.myLocation()


# Team Name: TEAM NINJA
# Members: Joshua Therence Templo, Niña Jane Campaner, Marverick Catigbe, Hannah Jamaica Vega
