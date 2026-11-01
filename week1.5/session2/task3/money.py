# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds : int, pence: int):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if (not isinstance(pounds, int) or not isinstance(pence, int)):
            raise TypeError("Not an integer")
        elif (pounds < 0 or pence < 0 or pence > 99):
            raise ValueError("Not within range")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """

        return f"£{self.pounds}.{str(self.pence).zfill(2)}"
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

    def __add__(self, other: Money):
        """
        Adds this Money to another Money, returning the total.
        """

        if not isinstance(other, Money):
            raise TypeError("Not able to add to non-money type!")

        if (self.pence + other.pence > 99):
            return Money(self.pounds + other.pounds + 1, self.pence + other.pence - 100)
        else:
            return Money(self.pounds + other.pounds, self.pence + other.pence)
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
