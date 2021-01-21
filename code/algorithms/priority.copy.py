def Priority(items, length, board_size, vehicles, heuristic):
    """A function that uses a Priority Cue search, which prioritizes states based on a heuristic."""

    # number of free spaces ahead of the target car
    if heuristic == 'H1':
        items = [[board, board.X_row_free()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        sorted_list = [item[0] for item in sorted_items]

    # number of vehicles blocking the target car
    elif heuristic == 'H2':
        items = [[board, len(board.blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # number distance to the goal position for the target car
    elif heuristic == 'H3':
        items = [[board, board.goal_distance()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # number of vehicles blocking the target car + the distance to the goal position
    elif heuristic == 'H4':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance()] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # number of blocking vehicles + distance to goal position + number of blocked blocking vehicles
    elif heuristic == 'H5':
        items = [[board, len(board.blocking_vehicles()) + board.goal_distance() + len(board.blocked_blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # number of blocking vehicles + number of blocked blocking vehicles
    elif heuristic == 'H6':
        items = [[board, len(board.blocked_blocking_vehicles()) + len(board.blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    # Most possible moves per state 
    elif heuristic == 'H7': 
        items_tuple = []
        for item in items: #items is list met alle states
            total_moves = sum(len(moves) for moves in item.pos_moves().values())
            items_tuple.append([item, total_moves])
    
        # Sort states per depth on most possible moves 
        sorted_items = sorted(items_tuple, key=lambda x: x[1], reverse=True) 
        sorted_list = [item[0] for item in sorted_items]
    
    # number of blocked blocking vehicles
    elif heuristic == 'H8':
        items = [[board, len(board.blocked_blocking_vehicles())] for board in items]
        sorted_items = sorted(items, key=lambda x: x[1], reverse=False)
        sorted_list = [item[0] for item in sorted_items]

    return sorted_list