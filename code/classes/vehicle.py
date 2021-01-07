class Vehicle(object):
    def __init__(self, name, orientation, row, col, length):
        self.orientation = orientation
        self.coordinates = (col - 1, row - 1)
        self.name = name
        self.length = length
