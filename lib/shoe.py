# lib/shoe.py
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # Set size using the setter
        self.condition = "New"  # Set initial condition to "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._size = value
        else:
            print("size must be an integer")  # Print error instead of raising exception

    def cobble(self):
        self.condition = "New"  # Set the condition to "New" after repair
        print("Your shoe is as good as new!")
