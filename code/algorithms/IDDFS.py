###############################################################
# IDDFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# TODO.
###############################################################

# anytree: https://pypi.org/project/anytree/
from anytree import Node, RenderTree
import copy
import time
from .BFS import BFS


class DFS(BFS):
    def __init__(self, board, max_depth=100):
        BFS.__init__(self, board)
        self.max_depth = max_depth

    def get_next_state(self):
        return self.states.pop()

    def run(self):  
        """Runs the algorithm until all possible states are checked."""

        while self.states != []: 
            new_board = self.get_next_state()
            # print(len(new_board.moves))
            if len(new_board.moves) >= self.max_depth:
                return None, self.state_space

            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space
            else: 
                print("possible moves")
                print(new_board.pos_moves())
                self.build_children(new_board) # lijst vullen met kids

                print(len(self.states))
                print([a.moves[0:2] for a in self.states])

class IDDFS:
    def __init__(self, board, max_depth):
        self.max_depth = max_depth
        self.board = board
        self.winning_board = None

    def run(self):
        for depth in range(1, self.max_depth):
            print(f"depth: {depth}")
            depth_first = DFS(self.board, depth)
            winning_board, states = depth_first.run()
            if winning_board is not None:
                return winning_board, states

        return winning_board, states
