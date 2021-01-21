###############################################################
# priority.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a priority on a queue of states. 
# The priority queue can also be pruned, using a beam. 
# Multiple heuristics can ben chosen from. 
# It returns a list with in the front the priority states. 
###############################################################

def Priority(items, length, board_size, vehicles, heuristic, beam):
    """A function that uses a Priority queue search, which prioritizes states based on a heuristic."""

    # number of free spaces ahead of the target car
    if heuristic == 'H1':
        items = [[board, board.X_row_free()] for board in items]

    # number of vehicles blocking the target car
    elif heuristic == 'H2':
        items = [[board, len(board.blocking_vehicles())] for board in items]

    # number distance to the goal position for the target car
    elif heuristic == 'H3':
        items = [[board, board.goal_distance()] for board in items]

    # number of vehicles blocking the target car + the distance to the goal position
    elif heuristic == 'H4':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance()] for board in items]

    # number of blocking vehicles + distance to goal position + number of blocked blocking vehicles
    elif heuristic == 'H5':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance() + len(board.blocked_blocking_vehicles())] for board in items]

    # number of blocking vehicles + number of blocked blocking vehicles
    elif heuristic == 'H6':
        items = [[board, len(board.blocked_blocking_vehicles()) + len(board.blocking_vehicles())] for board in items]

    # Most possible moves per state 
    elif heuristic == 'H7': 
        items_tuple = []
        for item in items: #items is list met alle states
            total_moves = sum(len(moves) for moves in item.pos_moves().values())
            items = items_tuple.append([item, total_moves])
    
    # number of blocked blocking vehicles
    elif heuristic == 'H8':
        items = [[board, len(board.blocked_blocking_vehicles())] for board in items]

    # first trying the biggest possible move for every vehicle 
    #elif heuristic == 'H9': 
        # nu moet die nog gaan sorteren op zoveel mogelijk moves... 
        # items = [[board, board.reversed_pos_moves()] for board in items]
    
    # sort list  
    if heuristic == 'H1' or 'H7' or 'H9': 
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        sorted_list = [item[0] for item in sorted_items]
    else: 
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # check for beam, else use priority 
    if beam: 
        beam_width = round((board_size ^ 2) / (7 * 7) * 10000)
        return sorted_list[:beam_width]
    
    return sorted_list