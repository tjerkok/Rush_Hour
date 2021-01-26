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
        """Loads in all needed information for the board."""
        self.vehicles = vehicles
        self.boardsize = boardsize
        self.board = []
        self.possible_moves = {}
        self.moves = []

    def load_board(self):
        """Loads the boards with the vehicles."""
        self.board = list(self.board)
        self.board.clear()
        cols = []

        # uses the boardsize to fill the array with underscores
        if self.boardsize < 10:
            for col in range(self.boardsize):
                cols.append('_')
        else:
            for col in range(self.boardsize):
                cols.append('__')

        for row in range(self.boardsize):
            self.board.append(cols)

        self.board = np.array(self.board, dtype='U25')

        # for loop to fill the array with vehicle names
        for vehicle in self.vehicles.values():
            x, y = vehicle.coordinates[0], vehicle.coordinates[1]

            self.fill_names(vehicle, len(vehicle.name), x, y)

        return self.board

    def fill_names(self, vehicle, name_length, x, y):
        """Fills the array with vehicle names depending on orientation."""
        if vehicle.orientation == 'H':
            x_index = 1
            y_index = 0
        else:
            x_index = 0
            y_index = 1

        # adds the vehicle names to the board
        if name_length < 2 and self.boardsize >= 10:
            for i in range(vehicle.length):
                self.board[y + i * y_index, x + i * x_index] = f'{vehicle.name} '
        else:
            for i in range(vehicle.length):
                self.board[y + i * y_index, x + i * x_index] = vehicle.name

    def pos_moves(self):
        """Creates a dict with a list of all possible moves per vehicle."""
        # for all vehicles in the board find the possible moves
        for vehicle in self.vehicles.values():
            self.possible_moves[vehicle.name] = []

            x, y = vehicle.coordinates[0], vehicle.coordinates[1]

            self.fill_possible_moves(vehicle, x, y)

        return self.possible_moves

    def fill_possible_moves(self, vehicle, x, y):
        """Fills possible moves dictionary depending on orientation."""
        # defines a string for the empty space
        if self.boardsize < 10:
            empty = '_'
        else:
            empty = '__'

        if vehicle.orientation == 'H':
            x_index = 1
            y_index = 0
            front, back = x, self.boardsize - (x + vehicle.length)
        else:
            x_index = 0
            y_index = 1
            front, back = y, self.boardsize - (y + vehicle.length)

        # fills the possible moves dictionary for the empty spaces in the front
        for i in range(1, front + 1):
            if self.board[y - i * y_index, x - i * x_index] == empty:
                self.possible_moves[vehicle.name].append(-i)
            else:
                break

        # fills the possible moves dictionary for the empty spaces in the back
        for i in range(1, back + 1):
            if self.board[y + (vehicle.length - 1 + i) * y_index,
                          x + (vehicle.length - 1 + i) * x_index] == empty:
                self.possible_moves[vehicle.name].append(i)
            else:
                break

    def X_row_free(self):
        """Returns the amount of free spaces ahead of the target car."""
        coordinates = self.vehicles['X'].coordinates
        row = self.board[coordinates[1]]

        if self.boardsize < 10:
            return list(row[coordinates[0]:]).count('_')
        else:
            return list(row[coordinates[0]:]).count('__')

    def blocking_vehicles(self):
        """Returns the amount of vehicles bloacking the target car."""
        x_row = self.vehicles['X'].coordinates[1]
        x_col = self.vehicles['X'].coordinates[0]

        # adds vehicles that are in the way of the target car to the array
        blocking_vehicles = []
        for vehicle in self.vehicles:
            if self.vehicles[vehicle].orientation == 'V':
                vehicle_col = self.vehicles[vehicle].coordinates[0]
                vehicle_row = self.vehicles[vehicle].coordinates[1]

                if vehicle_row == x_row or vehicle_row + 1 == x_row:
                    if vehicle_col > (x_col + 1):
                        blocking_vehicles.append(vehicle)

        return blocking_vehicles

    def goal_distance(self):
        """Returns the amount of distance the target car still has to move."""
        distance = self.boardsize - 2 - self.vehicles['X'].coordinates[0]

        return distance

    def blocked_blocking_vehicles(self, blocking=None):
        """Returns the vehicles that block the blocked vehicles."""
        if blocking is None:
            blocking = self.blocking_vehicles()
            self.visited = []

        # for all vehicles add the ones that block to the array
        blocking_vehicles = []
        for blocked_vehicle in blocking:
            col = self.vehicles[blocked_vehicle].coordinates[0]
            row = self.vehicles[blocked_vehicle].coordinates[1]
            length = self.vehicles[blocked_vehicle].length

            for vehicle in [vehicle for vehicle in self.vehicles if (
                            vehicle not in self.visited)]:
                vehicle_col = self.vehicles[vehicle].coordinates[0]
                vehicle_row = self.vehicles[vehicle].coordinates[1]
                vehicle_length = self.vehicles[vehicle].length

                self.fill_blocking_vehicles(blocking_vehicles, blocked_vehicle,
                                            vehicle, col, row, length,
                                            vehicle_col, vehicle_row,
                                            vehicle_length)

        return blocking_vehicles

    def fill_blocking_vehicles(self, blocking_vehicles, blocked_vehicle,
                               vehicle, col, row, length,
                               vehicle_col, vehicle_row,
                               vehicle_length):
        """Fills the blocking_vehicles array depending on orientation."""
        # defines the first and second part for the if statement
        if self.vehicles[blocked_vehicle].orientation == 'V':
            orientation = 'V'
            blocking_first = col
            blocking_second = row
            vehicle_first = vehicle_col
            vehicle_second = vehicle_row
        else:
            orientation = 'H'
            blocking_first = row
            blocking_second = col
            vehicle_first = vehicle_row
            vehicle_second = vehicle_col

        # appends blocking vehicles to the blocking_vehicles array
        if self.vehicles[vehicle].orientation == orientation:
            if vehicle_first == blocking_first:
                if vehicle_length == 2:
                    if vehicle_second + 2 == blocking_second or (
                       vehicle_second - length == blocking_second):
                        blocking_vehicles.append(vehicle)
                else:
                    if vehicle_second + 2 == blocking_second or (
                       vehicle_second + 3 == blocking_second) or (
                       vehicle_second - length == blocking_second):
                        blocking_vehicles.append(vehicle)
        else:
            if vehicle_second + 1 == blocking_second or (
               vehicle_second - length == blocking_second):
                if vehicle_length == 2:
                    if vehicle_first == blocking_first or (
                       vehicle_first + 1 == blocking_first):
                        blocking_vehicles.append(vehicle)
                else:
                    if vehicle_first == blocking_first or (
                       vehicle_first + 1 == blocking_first) or (
                       vehicle_col + 2 == blocking_first):
                        blocking_vehicles.append(vehicle)

    def MinMovesHeuristic(self):
        """Heuristic that makes use of the minimum required moves."""
        return self.MinimumRequiredMoves()

    def MinimumRequiredMoves(self):
        """Counts the minimum amount of moves the board has to make."""
        self.visited = ['X']

        blocked_vehicles = self.blocking_vehicles()

        for vehicle in blocked_vehicles:
            self.visited.append(vehicle)

        # find all the vehicles that block the blocking vehicles recursively
        while blocked_vehicles:
            blocked_vehicles = self.blocked_blocking_vehicles(blocked_vehicles)
            for vehicle in blocked_vehicles:
                self.visited.append(vehicle)

        # remove the duplicate vehicles
        no_duplicates_visited = []
        [no_duplicates_visited.append(visited) for visited in self.visited if (
         visited not in no_duplicates_visited)]

        min_required = len(no_duplicates_visited)

        return min_required

    def move(self, vehicle_name, shift, undo=False):
        """Moves a vehicle, if possible."""
        # if shift in self.possible_moves[vehicle_name]:
        if shift in self.pos_moves()[vehicle_name] or undo:
            vehicle = self.vehicles[vehicle_name]

            if vehicle.orientation == 'H':
                vehicle.coordinates = (vehicle.coordinates[0] + shift,
                                       vehicle.coordinates[1])
            else:
                vehicle.coordinates = (vehicle.coordinates[0],
                                       vehicle.coordinates[1] + shift)

            # add the moves for the board if we don't want to undo a move
            if not undo:
                self.moves.append([vehicle_name, shift])
            else:
                self.moves.pop(-1)

            self.load_board()
            return True

        return False

    def win(self):
        """Checks for win using vehicle X."""
        if self.vehicles['X'].coordinates[0] == self.boardsize - 2:
            return True
        else:
            return False
