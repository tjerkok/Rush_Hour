import csv
import re

from ...classes.board import Board
from ...classes.vehicle import Vehicle


def load_problem(filename):

    vehicles = {}
    with open(filename, newline='') as csvfile:
        match = re.search(r'\d+x', filename)
        board_size = int(str((match[0]))[:-1])
        r = csv.reader(csvfile, delimiter=',')
        next(r, None)
        for row in r:
            vehicle_name = row[0]
            orientation = row[1]
            vehicle_col = int(row[2])
            vehicle_row = int(row[3])
            vehicle_length = int(row[4])
            new_vehicle = Vehicle(vehicle_name, orientation, vehicle_row, vehicle_col, vehicle_length)
            vehicles[vehicle_name] = new_vehicle

    board = Board(vehicles, board_size)

    return board
