#########################################################
# vehicle.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Creates a vehicle object.
#########################################################


class Vehicle(object):
    """
    Class with all information about a vehicle.

    Attributes:
    Orientation: str (V(vertical)/H(horizontal))
    Coordinates: tuple(col, row)
    Name: str with name of vehicle (A t/m Z)
    Length: int with size of vehicle (car/truc)
    """

    def __init__(self, name, orientation, row, col, length):
        """Loads all information of the vehicle in the class."""
        self.name = name
        self.orientation = orientation
        self.coordinates = (col - 1, row - 1)
        self.length = length

    def __repr__(self):
        """Gives a representation of the object when it's printed."""
        return f"{self.name}, {self.orientation}, {self.coordinates}, {self.length}"
