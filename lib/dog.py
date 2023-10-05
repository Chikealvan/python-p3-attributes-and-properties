#!/usr/bin/env python3

# list of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # Initialize the Dog class with a name and breed
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    # Define a property for the 'name' attribute
    @property
    def name(self):
        return self._name

    # Setter method for 'name' attribute with validation
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    # Define a property for the 'breed' attribute
    @property
    def breed(self):
        return self._breed

    # Setter method for 'breed' attribute with validation using APPROVED_BREEDS
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

