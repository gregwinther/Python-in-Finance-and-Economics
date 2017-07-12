from airlines import *

# Making a new airline

BA = Airline()

BA.set_capacity(100)

print(BA.get_capacity())


# Generating demand curve and plotting

my_demand = DemandFunction()

my_demand.generate_uniform(20, 80)

my_demand.plot_demand()

your_demand = DemandFunction(300)

your_demand.generate_normal(50, 12)

your_demand.plot_demand()
