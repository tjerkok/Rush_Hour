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

#     possible_moves = board.pos_moves() for board in items

#    # Count all items within the lists in the values of the possible_moves dict https://www.geeksforgeeks.org/python-count-number-of-items-in-a-dictionary-value-that-is-a-list/ 
#     count_moves = 0 
#     for x in possible_moves: 
#         if isinstance(possible_moves[x], list): 
#             count_moves += len(possible_moves[x]) 
#     print(count_moves) 

#     #items = [[board, board.pos_moves()] for board in items]
#     items = [[board, count_moves] for board in items] #count_moves kan niet zo worden geitereerd...? 
#     sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
#     sorted_items = [item[0] for item in sorted_items]
    items_tuple = []
    for item in items:
        total_moves = sum(len(car) for moves in item.pos_moves().values() for car in moves.values()) 
        # eerst wordt moves uit item.pos_moves() gepakt met for moves in item.pos_moves().values(), dus moves = dict([moves van auto a], [moves van auto b])
        # daarna wordt voor elke moves de car eruit gepakt, waardoor bijv. car = [-1, 1, 2], dus dan de som van alle lengtes van de cars
        # (dit heb ik neit zelf bedacht maar van internet geplukt hahaha)
        items_tuple.append([item, sum()])
        # dus items_tuple wordt een lijst met de state en dan het aantal moves [[state, 4], [state, 8], etc]

    sorted_list = sorted(items_tuple, key=lambda x: x[1], reverse=True) # sorteert de lijst op het tweede element in de tuple, dus het aantal mogelijke moves

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
            
