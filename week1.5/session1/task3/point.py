# Week 1.5, Session 1: Task 3

import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    # Add distance_to() method here
    def distance_to(self, p: Point):
        return math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    # (This will need a parameter representing another point)

# Finally, add code here to demonstrate use of Point
