#########################################################
# load_in.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Loads the csv file with the information of a gameboard.
#########################################################

import csv
import re

from ..classes.board import Board
from ..classes.vehicle import Vehicle


def load_problem(filename):
    """Loads the vehicles and the boardsize from the csv input file."""
    vehicles = {}
    with open(filename, newline='') as csvfile:
        # reads the boardsize from the name of the csvfile
        match = re.search(r'\d+x', filename)
        board_size = int(str((match[0]))[:-1])

        # reads the csv input file into vehicles dict
        read = csv.reader(csvfile, delimiter=',')
        next(read, None)
        for row in read:
            vehicle_name = row[0]
            orientation = row[1]
            vehicle_col = int(row[2])
            vehicle_row = int(row[3])
            vehicle_length = int(row[4])

            # use the vehicle class to add a new vehicle
            new_vehicle = Vehicle(vehicle_name, orientation, vehicle_row,
                                  vehicle_col, vehicle_length)
            vehicles[vehicle_name] = new_vehicle

    # use the board class to make the board
    board = Board(vehicles, board_size)

    return board
