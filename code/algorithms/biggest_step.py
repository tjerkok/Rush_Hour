###############################################################
# Biggest_step.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Class with the BFS combined with the heuristick 
# that the biggest possible move of a vehicle is checked first.
###############################################################

import copy
from .BFS import BFS

class Step(BFS):
    """
    Class to use the Breadth First Search combined with the heuristick of 
    performing the biggest possible move of a vehicle first.

    Attributes:
    BFS attributes.

    Methods:
    BFS methods.
    build_children: creates all possible child-states from the current state
    and adds them to the archive.
    """

   def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.pos_moves().items():
            if movelist: 
                if len(movelist) > 1:
                    # sort for the biggest amount of steps first
                    movelist = sorted(movelist, key=lambda x: abs(0-x), reverse=True)
                
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