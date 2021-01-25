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

# class Step(BFS): 

#    def build_children(self, board):
#         """Creates all possible child-states."""
#         for vehicle, movelist in board.reversed_pos_moves().items():
#             for vehicle_move in movelist:
#                 child = copy.deepcopy(board)
#                 if not child.move(vehicle, vehicle_move):
#                     print("invalid move")
#                     return False

#                 if child.win() and self.lookahead:
#                     self.winning_board = child
#                     return True
#                 self.add_to_archive(child)

#         return False

class Step(BFS): 
    """ TODO """
    def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.pos_moves().items():
            for vehicle_move in [movelist[-1], movelist[0]]:
                if vehicle_move != movelist[-1]: #dubbel
                    child = copy.deepcopy(board)
                    if not child.move(vehicle, vehicle_move):
                        print("invalid move")
                        return False

                    if child.win() and self.lookahead:
                        self.winning_board = child
                        return True
                    self.add_to_archive(child)

        for vehicle, movelist in board.pos_moves().items():
            if len(movelist) > 2:
                for vehicle_move in movelist[1:-1]:
                    child = copy.deepcopy(board)
                    if not child.move(vehicle, vehicle_move):
                        print("invalid move")
                        return False

                    if child.win() and self.lookahead:
                        self.winning_board = child
                        return True
                    self.add_to_archive(child)

        return False

# [-2, -1, 1, 2, 3]
# [1]
