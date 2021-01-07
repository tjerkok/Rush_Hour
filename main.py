import csv
from code.classes.board import Board
from code.classes.vehicle import Vehicle
from sys import argv

if __name__ == '__main__':

    vehicles = {}
    with open('gameboards/Rushhour9x9_4.csv', newline='') as csvfile:
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

    board = Board(vehicles, 9)     #hardcoded
    print(board.load_board())

print(board.pos_moves())

moves = {'A': -1,
         'B': 1,
         'C': 2}

with open('output/output.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    w.writerow(['car', 'move'])
    for key in moves:
        w.writerow([key, moves[key]])
