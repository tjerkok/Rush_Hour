import csv
from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.visualization.visualization import visualize
from sys import argv
import re

if __name__ == '__main__':

    # Check command line arguments and load requested board
    if len(argv) == 2:
        filename = argv[1]
    else: 
        print("Usage: python3 main.py [gameboards/Rushhour9x9_4.csv]")
        exit(1)

    #filename = 'gameboards/Rushhour9x9_4.csv' # needs to be the commandline argument
    vehicles = {}
    with open(filename, newline='') as csvfile:
        match = re.search(r"\dx\d", filename)
        board_size = int(match[0][0])
        r = csv.reader(csvfile, delimiter=',')
        next(r, None)
        for row in r:
            vehicle_name = row[0]
            orientation = row[1]
            vehicle_row = int(row[3])
            vehicle_col = int(row[2])
            vehicle_length = int(row[4])
            new_vehicle = Vehicle(vehicle_name, orientation, vehicle_row, vehicle_col, vehicle_length)
            vehicles[vehicle_name] = new_vehicle

    board = Board(vehicles, board_size)     # hardcoded
    visualize(board.load_board())   # result in code/visualization/test.png


# print(board.pos_moves())

moves = {'A': -1,
         'B': 1,
         'C': 2}

with open('output/output.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    w.writerow(['car', 'move'])
    for key in moves:
        w.writerow([key, moves[key]])
