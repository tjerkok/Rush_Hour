###############################################################
# BFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function with Breadth First Search algorithm for Rush Hour game.
###############################################################

from ..classes.board import Board
import queue
import copy


def BFS(board, max_depth = 10):
    """Function that plays the Rush Hour game with a Breadth First Search algorithm"""

    BFS_queue = queue.Queue()
    BFS_queue.put(board)
    boards_visited = set()
    while not BFS_queue.empty():
        state = BFS_queue.get()
        print(len(state.moves))
        if not state.win():
            # print(state.pos_moves())
            for i, j in state.pos_moves().items():
                for k in j:
                    child = copy.deepcopy(state)
                    # print("i: ")
                    # print(i)
                    # print(k)
                    child.move(i, k)
                    child_board = child.load_board()
                    child_board.flags.writeable = False
                    hashed_child = hash(child_board.tostring())
                    if hashed_child not in boards_visited:
                        boards_visited.add(hashed_child)
                        # print(child.load_board())
                        BFS_queue.put(child)
        else:
            winning_board = state
            states = BFS_queue.qsize()
            BFS_queue = queue.Queue()

    return winning_board, states