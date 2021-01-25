###############################################################
# Biggest_step.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# TODO.
###############################################################
# import copy
# from .BFS import BFS

# class Step(BFS): 

# #    def build_children(self, board):
# #         """Creates all possible child-states."""
# #         for vehicle, movelist in board.reversed_pos_moves().items():
# #             for vehicle_move in movelist:
# #                 child = copy.deepcopy(board)
# #                 if not child.move(vehicle, vehicle_move):
# #                     print("invalid move")
# #                     return False

# #                 if child.win() and self.lookahead:
# #                     self.winning_board = child
# #                     return True
# #                 self.add_to_archive(child)

# #         return False

#    def build_children(self, board):
#         """Creates all possible child-states."""
#         for vehicle, movelist in board.pos_moves().items():
#              #abs(x-y) geeft het verschil tussen x en y --> het grootste verschil met 0 moet eerst worden gecheckt en voorin de queue gezet worden
#             min_move = min(movelist)
#             max_move = max(movelist)
#             if abs(0 - min_move) <= abs(0 - max_move): 
#                 # stop max_move voorin de queue en sorteer op grootste stappen eerst 
#             else: 
#                 # stop min_move voorin de queue en sorteer op kleinste stappen eerst
            

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

#     #    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
#     #     sorted_list = [item[0] for item in sorted_items]