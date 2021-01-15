###############################################################
# BFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function with Breadth First Search algorithm for Rush Hour game.
###############################################################

from ..classes.board import Board
from .beam import Beam
import queue
import copy


def BFS(board, beam, max_depth = 10):
    """Function that plays the Rush Hour game with a Breadth First Search algorithm"""

    BFS_queue = queue.Queue()
    BFS_queue.put(board)
    boards_visited = set()
    states = 0
    move = 0

    while not BFS_queue.empty():
        state = BFS_queue.get()
        if move < len(state.moves):
            print(len(state.moves))
            if beam:
                beamed_list = Beam(list(BFS_queue.queue), board.boardsize, len(board.vehicles))
                BFS_queue = queue.Queue()
                [BFS_queue.put(item) for item in beamed_list]
            if priority:
                priority_list = Priority(BFS_queue.queue)
            move = len(state.moves)

        if not state.win():
            for vehicle, movelist in state.pos_moves().items():
                for vehicle_move in movelist:
                    child = copy.deepcopy(state)
                    states += 1
                    child.move(vehicle, vehicle_move)
                    child_board = child.load_board()
                    child_board.flags.writeable = False
                    hashed_child = hash(child_board.tostring())
                    if hashed_child not in boards_visited:
                        boards_visited.add(hashed_child)
                        BFS_queue.put(child)
        else:
            winning_board = state
            BFS_queue = queue.Queue()

    return winning_board, states