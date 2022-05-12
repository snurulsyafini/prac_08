from car import Car
from random import randint


class UnreliableCar(Car):
    """Making an unreliable car settings"""

    def __init__(self, name, fuel, reliability):
        """Start UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive Unreliable Car sometimes"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
