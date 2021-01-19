###############################################################
# IDDFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# TODO.
###############################################################

# anytree: https://pypi.org/project/anytree/
from anytree import Node, RenderTree
import copy

def IDDFS(board):
    """Function that uses the Iterative Deepening Depth First Search algorithm."""
    for depth in range(1, 11):
        winning_board, states = DLS(board, depth)
        if winning_board is not None:
            return winning_board, states

    return winning_board, states

# [['A', 1], ['C', -1], ['E', -1], ['F', -3], ['B', 3], ['G', -2], ['D', 2], ['X', 3]]
def DLS(board, depth):  
    """Function that uses the Depth First Search algorithm."""
    BFS_stack = [board]
    boards_visited = set()
    states = 1

    while len(BFS_stack) > 0:
        state = BFS_stack.pop()
        # if len(state.moves) == 8:
        #     print([a.moves for a in BFS_stack if a.moves[0:1] == [['A', 1]]])
        # if len(state.moves) == 2:
        #     if state.moves == [['A', 1], ['C', -1]]:
        #         print("got good state")
        #         print(f"len(statemoves): {len(state.moves)}, depth: {depth}")

        if len(state.moves) < depth:
            for vehicle, movelist in state.pos_moves().items():
                for vehicle_move in movelist:

                    if not state.move(vehicle, vehicle_move):
                        print("invalid move")
                    else:
                        state_board = state.load_board()
                        state_board.flags.writeable = False
                        hashed_state = hash(state_board.tostring())
                        if hashed_state not in boards_visited:
                            boards_visited.add(hashed_state)
                            BFS_stack.append(copy.deepcopy(state))
                            states += 1


                        if state.win():
                            BFS_stack = []
                            winning_board = state
                            return winning_board, states

                        else:
                            state.move(vehicle, -vehicle_move, True)
                            state.load_board()
                            state.pos_moves()
                            winning_board = None


    return winning_board, states
