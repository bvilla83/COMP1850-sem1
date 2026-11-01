# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth: date):
        """
        Initialises two fields of the Person (name and birthday)
        """
        if (not isinstance(name, str)):
            raise TypeError("Name is not a string!")
        elif (name == ""):
            raise ValueError("Name needs to be filled in")

        if (not isinstance(birth, date)):
            raise TypeError("Birth is not a date object!")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Returns the initials of the name in uppercase
        """
        names = self.name.split(" ")

        letters = ""
        for name in names:
            letters += name[0].upper()

        return letters

    def is_birthday(self):
        """
        Returns True if Person's birthday is today, otherwise false
        """
        if self.birth == date.today():
            return True
        else:
            return False

