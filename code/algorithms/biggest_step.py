###############################################################
# Biggest_step.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Class with the BFS combined with the heuristic 
# that only the biggest possible move of every vehicle is 
# checked. 
###############################################################

import copy

from .BFS import BFS


class Step(BFS):
    """
    Class to use the Breadth First Search combined with the heuristic of 
    performing the biggest possible move of every vehicle.  

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
            # movelist cannot be empty and only if car isn't moved in last move
            if movelist and (not board.moves or board.moves[-1][0] != vehicle):

                # sort for the biggest steps first and make child
                movelist = sorted(movelist, key=lambda x: abs(0-x), reverse=True)
                child = copy.deepcopy(board)

                # move vehicle 
                if not child.move(vehicle, movelist[0]):
                    print("invalid move")
                    return False

                if child.win() and self.lookahead:
                    self.winning_board = child
                    return True

                self.add_to_archive(child)

        return False