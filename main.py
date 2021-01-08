import re
import csv

from code.classes.board import Board
from code.classes.vehicle import Vehicle
from code.algorithms import randomise, play_yourself, shortest_winning_testboard
from code.visualization.visualization import visualize
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2:
        filename = argv[1]
    else: 
        print("Usage: python3 main.py [gameboards/Rushhour9x9_4.csv]")
        exit(1)

    vehicles = {}
    with open(filename, newline='') as csvfile:
        match = re.search(r"\d+x", filename)
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
    visualize(board.load_board())   # result in code/visualization/test.png

    # --------------------------- Random choice --------------------------

    moves = randomise.random_moves_algorithm(board)

    moves_needed = len(moves)
    print(moves_needed)

    # --------------------------- Play yourself --------------------------

    #moves = play_yourself.play(board)

    # --------------------------- Shortest Winning game testboard (hardcoded) --------------------------

    #moves = shortest_winning_testboard.winning_moves(board)

    #moves_needed = len(moves)
    #print(moves_needed)

    # --------------------------- Output --------------------------

    with open('output/output.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['car', 'move'])
        for move in moves:
            w.writerow(move)
