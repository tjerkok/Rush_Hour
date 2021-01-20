###############################################################
# beam.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a beam on a list of states. The list can be
# a queue and stack, but has to be of type list. The size of
# the beam is determined by the size of the board and the
# amount of vehicles.
# Returns the beamed list.
###############################################################


def Beam(items, length, board_size, vehicles, heuristic):
    """Function that uses Beam Search with the most empty spaces ahead of the target car."""

    # 1 13 6 0.9
    # 2 13 6 0.9
    # 3 9 6 0.75
    # beam_ratio = (vehicles * 2.5) / (board_size * board_size)
    # print(f"queue length: {length}")

    if length < 10:
        beam_ratio = 0.95
    elif length >= 10 and length < 50:
        beam_ratio = 0.85
    elif length >= 50 and length < 500:
        beam_ratio = 0.7
    elif length >= 500 and length < 1000:
        beam_ratio = 0.5
    elif length >= 1000 and length < 5000:
        beam_ratio = 0.3
    elif length >= 5000:
        beam_ratio = 0.25

    beam = round(len(items) * beam_ratio)

    # number of free spaces ahead of the target car
    if heuristic == 'H1':
        items = [[board, board.X_row_free()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        sorted_items = [item[0] for item in sorted_items]

    # number of vehicles blocking the target car
    elif heuristic == 'H2':
        items = [[board, len(board.blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_items = [item[0] for item in sorted_items]

    # number distance to the goal position for the target car
    elif heuristic == 'H3':
        items = [[board, board.goal_distance()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_items = [item[0] for item in sorted_items]

    # number of vehicles blocking the target car + the distance to the goal position
    elif heuristic == 'H4':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_items = [item[0] for item in sorted_items]

    # number of blocking vehicles + distance to goal position + number of blocked blocking vehicles
    elif heuristic == 'H5':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance() + len(board.blocked_blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_items = [item[0] for item in sorted_items]

    # number of blocking vehicles + number of blocked blocking vehicles
    elif heuristic == 'H6':
        items = [[board, len(board.blocked_blocking_vehicles()) + len(board.blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_items = [item[0] for item in sorted_items]

    return sorted_items[:beam]
