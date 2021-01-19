###############################################################
# BFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function with Breadth First Search algorithm for Rush Hour game.
###############################################################

from .beam import Beam
from .priority import Priority
import copy
import time

class BFS:
    def __init__(self, board, beam, priority, heuristic):
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.boards_visited = set()
        self.winning_board = None
        self.state_space = 1
        self.beam = beam
        self.priority = priority
        self.heuristic = heuristic

    def get_next_state(self):
        """Gets the next state from the list of states."""
        return self.states.pop(0)

    def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.pos_moves().items():
            for vehicle_move in movelist:
                child = copy.deepcopy(board)
                if not child.move(vehicle, vehicle_move):
                    print("invalid move")
                    return False
                self.add_to_archive(child)
                self.state_space += 1

    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()
        board_array.flags.writeable = False 
        hashed_board = hash(board_array.tostring())
        if hashed_board not in self.boards_visited:
            self.boards_visited.add(hashed_board)
            self.states.append(board)

    def combine_algorithm(self, beam, priority): 
        """Combines the Beam search or the Priority search with the BFS."""
        if beam:
            beamed_list = Beam(self.states, length, board.boardsize, len(board.vehicles), self.heuristic)
            self.states.append(beamed_list)
        if priority: # and move > apply_priority:
            priority_list = Priority(self.states)
            self.states.append(self.states)

    def run(self):  
        """Runs the algorithm untill all possible states are checked."""

        if self.beam or self.priority: 
            self.states.combine_algorithm()

        while self.states != []: 
            new_board = self.get_next_state()

            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space
            else: 
                self.build_children(new_board) # lijst vullen met kids

        # if queue empty but not won, return None board
        return None, self.state_space