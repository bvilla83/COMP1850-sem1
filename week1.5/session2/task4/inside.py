# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Circle, Point

p = Point(11, 3)
c = Circle(10, Point(0, 0))

if p in c:
    print("point inside circle!")