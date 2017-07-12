"""This module is used to make simple Bertrand games focused on airlines"""

class Airline:
    """Class for Airline. Getter and setter for capacity and price"""

    def __init__(self, capacity=0, price=0):
        self.capacity = capacity
        self.price = price

    def set_capacity(self, new_capacity):
        """Sets capacity"""
        self.capacity = new_capacity

    def set_price(self, new_price):
        """Sets price"""
        self.price = new_price

    def get_capacity(self):
        """Returns capacity"""
        return self.capacity

    def get_price(self):
        """Returns price"""
        return self.price


if __name__ == "__main__":
    
    # Test

    BA = Airline()

    BA.set_capacity(100)

    print(BA.get_capacity())
