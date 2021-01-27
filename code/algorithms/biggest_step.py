###############################################################
# Biggest_step.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Class with the BFS combined with the beam and the heuristick 
# that first the biggest possible move of a vehicle is checked.
###############################################################

import copy
from .BFS import BFS

class Step(BFS):

   def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.pos_moves().items():
            if movelist: 
                if len(movelist) > 1:
                    # sort for the biggest amount of steps first
                    movelist = sorted(movelist, key=lambda x: abs(0-x), reverse=True)
                # add beam
                beam_width = round((board.boardsize ^ 2) / (7 * 7) * 10000)
                for vehicle_move in movelist[:beam_width]:
                    child = copy.deepcopy(board)
                    if not child.move(vehicle, vehicle_move):
                        print("invalid move")
                        return False

                    if child.win() and self.lookahead:
                        self.winning_board = child
                        return True
                    self.add_to_archive(child)

        return False
