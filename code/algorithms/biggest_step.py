###############################################################
# Biggest_step.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# TODO.
###############################################################
import copy
from .BFS import BFS

class Step(BFS): 

   def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.reversed_pos_moves().items():
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
