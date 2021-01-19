###############################################################
# priority.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a priority on a queue of states. This uses the
# Heuristic that a board with the most possible moves is priority.
# It returns a list with in the front the priority states. 
###############################################################

def Priority(items):
    """A function that uses a Priority Cue search, which prioritizes the states with the most possible moves."""

    items_tuple = []
    for item in items:
        # Calculate total possible moves per state 
        total_moves = sum(len(moves) for moves in item.pos_moves().values())
        items_tuple.append([item, total_moves])
    
    # Sort states per depth on most possible moves 
    sorted_items = sorted(items_tuple, key=lambda x: x[1], reverse=True) 
    sorted_list = [item[0] for item in sorted_items]

    return sorted_list
