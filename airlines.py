"""This module is used to make simple Bertrand games focused on airlines"""

import numpy as np
from matplotlib import pyplot as plt

class Airline:
    """Class for Airline. Getter and setter for capacity and price"""

    def __init__(self, name="airline", capacity=0, price=0):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.seats_left = capacity

    def set_capacity(self, new_capacity):
        """Sets capacity"""
        self.capacity = new_capacity
        self.seats_left = new_capacity

    def set_price(self, new_price):
        """Sets price"""
        self.price = new_price

    def get_capacity(self):
        """Returns capacity"""
        return self.capacity

    def get_price(self):
        """Returns price"""
        return self.price

    def get_seats_left(self):
        """Returns remaining seats"""
        return self.seats_left

    def sell_ticket(self):
        """Reduces number of availables seats by 1"""
        self.seats_left -= 1

    def empty_airplane(self):
        """Empties plane: the number of seats left is set equal to capacity"""
        self.seats_left = self.capacity
    
    def get_name(self):
        """Returns name of airline"""
        return self.name

    def set_name(self, new_name):
        """Sets name of airline"""
        self.name = new_name

class DemandFunction:
    """Class that generates a demand function"""

    def __init__(self, N=100):
        self.no_consumers = N
        self.demand = np.array([])

    def generate_uniform(self, min_price, max_price):
        """Generates uniformly distributed demand function"""
        self.demand = np.random.uniform(min_price, max_price, self.no_consumers)

    def generate_normal(self, mean, standard_deviation):
        """Generates normal distributed demand function"""
        self.demand = np.random.normal(mean, standard_deviation, self.no_consumers)

    def get_demand(self):
        """Returns demand function"""
        return self.demand

    def set_demand(self, new_demand):
        """Sets demand"""
        self.demand = new_demand

    def plot_demand(self):
        """Cummulates demand function and plots"""

        # Preparing
        max_price = int(np.max(self.demand))
        min_price = int(np.min(self.demand))

        cummulative_demand = np.zeros(max_price - min_price)

        # Aggregating
        i = 0
        for price in range(min_price, max_price):

            cummulative_demand[i] = sum(price <= bid for bid in self.demand)
            i += 1

        # Plotting
        plt.plot(cummulative_demand, range(min_price, max_price))
        plt.xlabel("Q")
        plt.ylabel("P")
        plt.title("Demand")
        plt.show()

class AirlineMarket:
    """Class that is supposed to match consumers with airlines"""

    def __init__(self):
        self.airlines = []
        self.demand = DemandFunction()
        self.no_of_airlines = 0

    def add_airline(self, airline):
        """Adds airline to the market"""
        self.airlines.append(airline)
        self.no_of_airlines += 1

    def set_demand(self, demand):
        """Sets demand function"""
        self.demand = demand
    
    def get_demand(self):
        """Returns demand object"""
        return self.demand

    def allocate_tickets(self):
        """Market clearing function"""

        # Resetting airplanes
        for airline in self.airlines:
            airline.empty_airplane()

        '''
        for airline in self.airlines:
            print(airline.get_price())
        '''

        # Sorting airline prices by bubble sort
        swapped = True
        while swapped:
            swapped = False
            for i in range(self.no_of_airlines - 1):
                if self.airlines[i].get_price() > self.airlines[i + 1].get_price():
                    temp1 = self.airlines[i]
                    temp2 = self.airlines[i + 1]
                    self.airlines[i] = temp2
                    self.airlines[i + 1] = temp1
                    swapped = True

        # Tickets are sold
        temp_demand = np.sort(self.demand.get_demand())

        for airline in self.airlines:
            i = 0
            for consumer_price in temp_demand:

                if airline.get_seats_left() > 0:

                    if airline.get_price() < consumer_price:
                        airline.sell_ticket()
                        i += 1

            temp_demand = temp_demand[i: -1]

        print("--------------------")
        for airline in self.airlines:
            print("Airline: ", airline.get_name(),\
            "Seats left: ", airline.get_seats_left(), " Price: ", airline.get_price())
        print("--------------------")

if __name__ == "__main__":

    BA = Airline()
    IB = Airline()
    DY = Airline()

    DY.set_price(10)
    BA.set_price(25)
    IB.set_price(40)

    DY.set_capacity(50)
    BA.set_capacity(50)
    IB.set_capacity(50)

    bertrand_market = AirlineMarket()

    uniform_demand = DemandFunction()
    uniform_demand.generate_uniform(10,50)

    bertrand_market.set_demand(uniform_demand)

    bertrand_market.add_airline(IB)
    bertrand_market.add_airline(BA)
    bertrand_market.add_airline(DY)

    bertrand_market.allocate_tickets()
