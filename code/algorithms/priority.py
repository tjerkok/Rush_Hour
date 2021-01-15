###############################################################
# priority.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function to apply a priority on a queue of states. This uses the 
# Heuristic that a board with the most possible moves is priority. 
# item = queue with all states 
# It returns queue with in the front the priority cues. 
###############################################################

from ..classes.board import Board
import queue

def Priority(items): 
    """A function that uses a Priority Cue search, which prioritizes the states with the most possible moves.""" 

    possible_moves = [board.pos_moves() for board in items]

   # Count all items within the lists in the values of the possible_moves dict https://www.geeksforgeeks.org/python-count-number-of-items-in-a-dictionary-value-that-is-a-list/ 
    count_moves = 0 
    for x in possible_moves: 
        if isinstance(possible_moves[x], list): 
            count_moves += len(possible_moves[x]) 
    print(count_moves) 

    #items = [[board, board.pos_moves()] for board in items]
    items = [[board, count_moves] for board in items] #count_moves kan niet zo worden geitereerd...? 
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    sorted_items = [item[0] for item in sorted_items]

    # Prioritize https://www.geeksforgeeks.org/priority-queue-in-python/ 
    # try: 
    #     max = 0 
    #     for i in range(len(possible_moves)): 
    #         if possible_moves[i] > possible_moves[max]:
    #             max = i 
    #     item = possible_moves[max]
    #     del possible_moves[max]
    #     return item
    # except IndexError:
    #     print()
    #     exit()
            
