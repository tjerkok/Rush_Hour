###############################################################
# priority.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a priority on a list of states.
# The priority queue can also be pruned, using a beam.
# Multiple heuristics can ben chosen from.
# It returns a list with in the front the priority states.
###############################################################


def Priority(items, board_size, heuristic, beam):
    """A function that prioritizes states based on a heuristic."""
    # maximal number of free spaces ahead of the target car
    if heuristic == 'H1':
        items = [
            [board, board.X_row_free()] for board in items
            ]

    # minimum number of vehicles blocking the target car
    elif heuristic == 'H2':
        items = [
            [board, len(board.blocking_vehicles())] for board in items
            ]

    # minimum distance to the goal position for the target car
    elif heuristic == 'H3':
        items = [
            [board, board.goal_distance()] for board in items
            ]

    # H2 + H3
    elif heuristic == 'H4':
        items = [
            [board, len(board.blocking_vehicles()) +
             board.goal_distance()] for board in items
            ]

    # H2 + H3 + H8
    elif heuristic == 'H5':
        items = [
            [board, len(board.blocking_vehicles()) +
             board.goal_distance() +
             len(board.blocked_blocking_vehicles())] for board in items
            ]

    # H2 + H8
    elif heuristic == 'H6':
        items = [
            [board, len(board.blocked_blocking_vehicles()) +
             len(board.blocking_vehicles())] for board in items
            ]

    # most possible moves per state
    elif heuristic == 'H7':
        items_tuple = []
        for item in items:
            total_moves = sum(
                len(moves) for moves in item.pos_moves().values()
                )
            items_tuple.append([item, total_moves])
        items = items_tuple

    # minimum number of blocked blocking vehicles
    elif heuristic == 'H8':
        items = [
            [board, len(board.blocked_blocking_vehicles())] for board in items
            ]

    # minimum number of required moves
    elif heuristic == 'H9':
        items = [
            [board, board.MinMovesHeuristic()] for board in items
            ]
        print(items[1])

    # sort states per depth
    if heuristic in ('H1', 'H7'):
        # sort by maximum
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        sorted_list = [item[0] for item in sorted_items]
    else:
        # sort by minimum
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # check for beam, else use priority
    if beam:
        beam_width = round((board_size ^ 2) / (7 * 7) * 10000)
        return sorted_list[:beam_width]

    return sorted_list
