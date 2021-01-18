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
 
    # total_moves = 0
    # count = 0
    items_tuple = []
    for item in items:
        total_moves = sum(len(moves) for moves in item.pos_moves().values())

        items_tuple.append([item, total_moves])

    sorted_items = sorted(items_tuple, key=lambda x: x[1], reverse=True) # sorteert de lijst op het tweede element in de tuple, dus het aantal mogelijke moves
    sorted_list = [item[0] for item in sorted_items]

    return sorted_list

    # item.pos_moves().values() geeft per state per vehicle een lijst met alle possible moves
    # eerst wordt moves uit item.pos_moves() gepakt met for moves in item.pos_moves().values(), dus moves = dict([moves van auto a], [moves van auto b])
    # daarna wordt voor elke moves de car eruit gepakt, waardoor bijv. car = [-1, 1, 2], dus dan de som van alle lengtes van de cars
    # dus items_tuple wordt een lijst met de state en dan het aantal moves [[state, 4], [state, 8], etc]
