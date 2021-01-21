####################################################################
# BFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Class with Breadth First Search algorithm for Rush Hour game.
#####################################################################

from .beam import Beam
from .priority import Priority
import copy
import time
from sys import getsizeof

class BFS:
    def __init__(self, board, beam=False, priority=False, heuristic='H1', lookahead=True):
        self.board = copy.deepcopy(board)
        self.boardsize = board.boardsize
        self.vehicle_length = len(board.vehicles)
        self.states = [copy.deepcopy(self.board)]
        self.boards_visited = set()
        self.winning_board = None
        self.state_space = 1
        self.beam = beam
        self.priority = priority
        self.heuristic = heuristic
        self.lookahead = lookahead
        self.move = 0
        self.apply_priority = 0  #round(2.33 * self.boardsize)

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

                if child.win() and self.lookahead:
                    self.winning_board = child
                    return True
                self.add_to_archive(child)

        return False

    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()
        board_array.flags.writeable = False
        hashed_board = hash(board_array.tostring())
        if hashed_board not in self.boards_visited:
            self.boards_visited.add(hashed_board)
            self.states.append(board)
            self.state_space += 1

        """ Dictionary ## langzamer doordat die meer staten doorgaat? of omdat die langzamer door de staten gaat. 
        if hashed_board in self.boards_visited:
            if self.boards_visited[hashed_board] > len(board.moves):
                self.boards_visited[hashed_board] = len(board.moves)
                self.states.append(board)
        else:
            self.boards_visited[hashed_board] = len(board.moves)
            self.states.append(board)
        """

    def combine_algorithm(self):
        """Combines the Beam search or the Priority search with the BFS."""
        # if self.beam:
        #     beamed_list = Beam(self.states, len(self.states), self.boardsize, self.vehicle_length, self.heuristic)
        #     self.states = beamed_list
        if self.beam: 
            beamed_list = Priority(self.states, len(self.states), self.boardsize, self.vehicle_length, self.heuristic, beam=True)
            self.states = beamed_list
        if self.priority:
            priority_list = Priority(self.states, len(self.states), self.boardsize, self.vehicle_length, self.heuristic, beam=False)
            self.states = priority_list

    def run(self):
        """Runs the algorithm untill all possible states are checked."""
        while self.states:

            new_board = self.get_next_state()
            if self.move < len(new_board.moves):
                if self.beam or (self.priority and self.move > self.apply_priority):
                    self.combine_algorithm()
                self.move = len(new_board.moves)

            if new_board.win():
                self.winning_board = new_board 
                return self.winning_board, self.state_space
            else:
                if self.build_children(new_board): # lijst vullen met kids, build_children() returnt True if child.win() dankzij lookahead
                    return self.winning_board, self.state_space

        # if queue empty but not won, return None board
        return None, self.state_space
