class Bus:
    """define a color of a bus"""
    count = 0 #bus count

    def __init__(self, driver, color, seats):
        self.driver = driver
        self.num_of_seats = seats
        self.color = color
        self.bus_count()

    def set_color(self, color):
        self.color = color

    def num_of_seats(self, seats):
        self.seats = seats

    def bus_count(self):
        self.count = self.count + 1


bus = Bus("Prince", 26, "yellow")
bus.set_color("Blue") # Update the bus color.
bus.num_of_seats= 26 # Update the seats.
print(bus)
print(bus.count)

# Exercise 2


