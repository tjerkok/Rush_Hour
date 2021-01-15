###############################################################
# beam.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a beam on a list of states. The list can be
# a queue and stack, but has to be of type list. Returns the
# beamed list.
###############################################################

from ..classes.board import Board


def Beam(items, board_size, vehicles):
    """Function that uses Beam Search with the most empty spaces ahead of the target car."""

    # 1 13 6 0.9
    # 2 13 6 0.9
    # 3 9 6 0.75
    beam_ratio = (vehicles * 2.5) / (board_size * board_size)
    beam = round(len(items) * beam_ratio)
    items = [[board, board.X_row_free()] for board in items]
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    sorted_items = [item[0] for item in sorted_items]

    return sorted_items[:beam]
