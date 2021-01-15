#########################################################
# board.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Creates the board, moves vehicles and checks for win.
#########################################################

import numpy as np

class Board(object):
    """
    A class that initializes the gameboard, moves vehicles and checks for win.

    Attributes:
    vehicles: dict with all information about a vehicle
    boardsize: int with size of the board as stated in the name of the file
    board: empty list which get filled in other functions
    possible_moves: dict with all possible moves per vehicle

    Methods:
    load_board: loads the boards with the vehicles
    pos_moves: creates the possible_moves dict
    X_row_free: Returns the amount of free spaces ahead of the target car
    move: moves a vehicle, if possible
    win: checks for win, using vehicle X
    """

    def __init__(self, vehicles, boardsize):
        """Loads in all needed information for the board"""

        self.vehicles = vehicles
        self.boardsize = boardsize
        self.board = []
        self.possible_moves = {}
        self.moves = []

    def load_board(self):
        """Loads the boards with the vehicles"""

        self.board = list(self.board)
        self.board.clear()
        cols = []

        # Uses the boardsize from the filename
        if self.boardsize < 10:
            for col in range(self.boardsize):
                cols.append('_')
        else:
            for col in range(self.boardsize):
                cols.append('__')

        for row in range(self.boardsize):
            self.board.append(cols)

        self.board = np.array(self.board, dtype='U25')

        if self.boardsize < 10:
            for vehicle in self.vehicles.values():
                x, y = vehicle.coordinates[0], vehicle.coordinates[1]

                if vehicle.orientation == 'H':
                    for i in range(vehicle.length):
                        self.board[y, x + i] = vehicle.name
                else:
                    for i in range(vehicle.length):
                        self.board[y + i, x] = vehicle.name
        else:
            for vehicle in self.vehicles.values():
                x, y = vehicle.coordinates[0], vehicle.coordinates[1]

                if len(vehicle.name) < 2:
                    if vehicle.orientation == 'H':
                        for i in range(vehicle.length):
                            self.board[y, x + i] = f'{vehicle.name} '
                    else:
                        for i in range(vehicle.length):
                            self.board[y + i, x] = f'{vehicle.name} '
                else:
                    if vehicle.orientation == 'H':
                        for i in range(vehicle.length):
                            self.board[y, x + i] = vehicle.name
                    else:
                        for i in range(vehicle.length):
                            self.board[y + i, x] = vehicle.name

        return self.board

    def pos_moves(self):
        """Creates a dict with a list of all possible moves per vehicle"""

        for vehicle in self.vehicles.values():
            self.possible_moves[vehicle.name] = []

            if vehicle.orientation == 'H':
                left, right = vehicle.coordinates[0], self.boardsize - (vehicle.coordinates[0] + vehicle.length)

                if self.boardsize < 10:
                    for i in range(1, left + 1):
                        if self.board[vehicle.coordinates[1], vehicle.coordinates[0] - i] == '_':
                            self.possible_moves[vehicle.name].append(-i)
                        else:
                            break

                    for i in range(1, right + 1):
                        if self.board[vehicle.coordinates[1], vehicle.coordinates[0] + vehicle.length - 1 + i] == '_':
                            self.possible_moves[vehicle.name].append(i)
                        else:
                            break
                else:
                    for i in range(1, left + 1):
                        if self.board[vehicle.coordinates[1], vehicle.coordinates[0] - i] == '__':
                            self.possible_moves[vehicle.name].append(-i)
                        else:
                            break

                    for i in range(1, right + 1):
                        if self.board[vehicle.coordinates[1], vehicle.coordinates[0] + vehicle.length - 1 + i] == '__':
                            self.possible_moves[vehicle.name].append(i)
                        else:
                            break

            else:
                up, down = vehicle.coordinates[1], self.boardsize - (vehicle.coordinates[1] + vehicle.length)

                if self.boardsize < 10:
                    for i in range(1, up + 1):
                        if self.board[vehicle.coordinates[1] - i, vehicle.coordinates[0]] == '_':
                            self.possible_moves[vehicle.name].append(i)
                        else:
                            break

                    for i in range(1, down + 1):
                        if self.board[vehicle.coordinates[1] + vehicle.length - 1 + i, vehicle.coordinates[0]] == '_':
                            self.possible_moves[vehicle.name].append(-i)
                        else:
                            break
                else:
                    for i in range(1, up + 1):
                        if self.board[vehicle.coordinates[1] - i, vehicle.coordinates[0]] == '__':
                            self.possible_moves[vehicle.name].append(i)
                        else:
                            break

                for i in range(1, down + 1):
                    if self.board[vehicle.coordinates[1] + vehicle.length - 1 + i, vehicle.coordinates[0]] == '__':
                        self.possible_moves[vehicle.name].append(-i)
                    else:
                        break

        return self.possible_moves

    def serialize(self): 
        #serialized = ""
        # for vehicle in self.vehicles.values()
        #     serialized += f"({vehicle.value.name}, {vehicle.value.orientation}, {vehicle.value.coordinates}, {vehicle.value.length})." #Vehicle een ID geven?? 

        # return serialized 
        pass


    def unserialize(self, serial): 
        # for vehicle in serial.split(".").split().split()
        pass

    def X_row_free(self):
        """Returns the amount of free spaces ahead of the target car"""

        coordinates = self.vehicles['X'].coordinates
        row = self.board[coordinates[1]]

        if self.boardsize < 10:
            return list(row[coordinates[0]:]).count('_')
        else:
            return list(row[coordinates[0]:]).count('__')


    def move(self, vehicle_name, shift):
        """Moves a vehicle, if possible"""

        # if shift in self.possible_moves[vehicle_name]:
        if shift in self.pos_moves()[vehicle_name]:
            vehicle = self.vehicles[vehicle_name]

            if vehicle.orientation == 'H':
                vehicle.coordinates = (vehicle.coordinates[0] + shift, vehicle.coordinates[1])

            else:
                vehicle.coordinates = (vehicle.coordinates[0], vehicle.coordinates[1] - shift)

            self.moves.append([vehicle_name, shift])

            return True

        return False
    

    def win(self):
        """Checks for win, using vehicle X"""

        if self.vehicles['X'].coordinates[0] == self.boardsize - 2:
            return True
        else:
            return False
