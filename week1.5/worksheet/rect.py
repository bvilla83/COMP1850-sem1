# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width: int, height: int):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if (not isinstance(width, int) or not isinstance(height, int)):
            raise TypeError("Not valid type")
        elif (width <= 0 or height <= 0):
            raise ValueError("Invalid arguments")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """
        Checks if the rectangle is also a square (width = height)
        """
        if self.width == self.height: return True
        else: return False

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return (self.width + self.height) * 2
