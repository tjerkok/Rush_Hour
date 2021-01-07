import numpy as np 

class Board(object):
    def __init__(self, vehicles, boardsize):
        self.vehicles = vehicles
        self.carname = carname
        self.boardsize = boardsize
        self.board = []
        self.possible_moves = self.possible_moves(self)

    def load_board(self):
        cols = []
        for row in range(self.boardsize):
            cols.append(' ')
        for row in range(self.boardsize):
            self.board.append(cols)
        self.board = np.array(self.board)
        
        for vehicle in self.vehicles:
            x, y = vehicle.coordinates[0], vehicle.coordinates[1]
            if vehicle.orientation == "H":
                for i in range(vehicle.length):
                    self.board[y, x + 1] = vehicle.name
            else:
                for i in range(vehicle.length):
                    self.board[y + 1, x] = vehicle.name
        return self.board

    # 0 is also a possible move
    def possible_moves(self):
        self.possible_moves = {}
        for vehicle in self.vehicles:
            self.possible_moves[vehicle.name] = []
            if vehicle.orientation == "H":
                left, right = -vehicle.coordinates[0], self.boardsize - (vehicle.coordinates[0] + vehicle.length)
                for i in range(left, right + 1):
                    if self.board[vehicle.coordinates[1], vehicle.coordinates[0] + i] == '_':
                        self.possible_moves[vehicle.name].append(i)
            elif vehicle.orientation == "V":
                up, down = -vehicle.coordinates[1], self.boardsize - (vehicle.coordinates[1] + vehicle.length)
                for i in range(down, up + 1):
                    if self.board[vehicle.coordinates[1], vehicle.coordinates[0] + i] == '_':
                        self.possible_moves[vehicle.name].append(i)
        return self.possible_moves

    # load_board() instead of alternating part of board
    def move(self, vehicle_name, shift):
        if shift in self.possible_moves[vehicle_name]:
            vehicle = self.vehicles[vehicle_name]
            if vehicle.orientation == "H":
                vehicle.coordinates = (vehicle.coordinates[0] + shift, vehicle.coordinates[1])
            elif vehicle.orientation == "V":
                vehicle.coordinates = (vehicle.coordinates[0], vehicle.coordinates[1] + shift)
            print(self.load_board())
            return True

        return False

    def win(self):
        if self.vehicles.name == 'X' and self.vehicles.coordinates[1] == self.boardsize - 1:
            return True
        else:
            return False
