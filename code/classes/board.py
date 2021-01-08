################
#
#
#
################

import numpy as np

class Board(object):
    """
    A class that initializes the gameboard, moves vehicles and checks for win.
    
    Attributes: 
    vehicles: dict with all information about a vehicle.
    boardsize: int with size of the board as stated in the name of the file.
    board: list with...
    possible_moves: dict with all possible moves per vehicle.

    Methods: 
    load_board:
    pos_moves:
    move:
    win: 

    """ 

    def __init__(self, vehicles, boardsize):
        """ """ 
        self.vehicles = vehicles
        self.boardsize = boardsize
        self.board = []
        self.possible_moves = {}

    def load_board(self):
        """Loads the board and applies the vehicles."""
        self.board = list(self.board)
        self.board.clear()
        cols = []

        for col in range(self.boardsize):
            cols.append('_')

        for row in range(self.boardsize):
            self.board.append(cols)

        self.board = np.array(self.board)

        for vehicle in self.vehicles.values():
            x, y = vehicle.coordinates[0], vehicle.coordinates[1]

            if vehicle.orientation == "H":
                for i in range(vehicle.length):
                    self.board[y, x + i] = vehicle.name
            else:
                for i in range(vehicle.length):
                    self.board[y + i, x] = vehicle.name

        return self.board

    # 0 is also a possible move
    def pos_moves(self):
        """Creates a dict with a list of all possible moves per vehicle.""" 
        for vehicle in self.vehicles.values():
            self.possible_moves[vehicle.name] = []

            if vehicle.orientation == "H":
                left, right = vehicle.coordinates[0], self.boardsize - (vehicle.coordinates[0] + vehicle.length)

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
                up, down = vehicle.coordinates[1], self.boardsize - (vehicle.coordinates[1] + vehicle.length)

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

        return self.possible_moves

    # load_board() instead of alternating part of board
    def move(self, vehicle_name, shift):
        """Moves a vehicle, if possible.""" 
        if shift in self.possible_moves[vehicle_name]:
            vehicle = self.vehicles[vehicle_name]

            if vehicle.orientation == "H":
                vehicle.coordinates = (vehicle.coordinates[0] + shift, vehicle.coordinates[1])

            else:
                vehicle.coordinates = (vehicle.coordinates[0], vehicle.coordinates[1] - shift)

            return True

        return False

    def win(self):
        """Checks for win, using vehicle X."""
        if self.vehicles['X'].coordinates[0] == self.boardsize - 2:
            return True
        else:
            return False
