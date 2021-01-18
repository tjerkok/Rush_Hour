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
from .priority import Priority
import queue
import copy


def BFS(board, beam, priority, heuristic='H1'):
    """Function that plays the Rush Hour game with a Breadth First Search algorithm"""

    BFS_queue = queue.Queue()
    BFS_queue.put(board)
    boards_visited = set()
    states = 0
    move = 0
    apply_priority = round(2.33 * board.boardsize)

    while not BFS_queue.empty():
        state = BFS_queue.get()
        if move < len(state.moves):
            print(len(state.moves))
            if beam:
                beamed_list = Beam(list(BFS_queue.queue), board.boardsize, len(board.vehicles), heuristic)
                BFS_queue = queue.Queue()
                [BFS_queue.put(item) for item in beamed_list]
            if priority and move > apply_priority:
                priority_list = Priority(list(BFS_queue.queue))
                BFS_queue = queue.Queue()
                [BFS_queue.put(item) for item in priority_list]
            move = len(state.moves)

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
                        BFS_queue.put(copy.deepcopy(state))
                        states += 1

                    if state.win():
                        BFS_queue = queue.Queue()
                        winning_board = state
                    else:
                        state.move(vehicle, -vehicle_move, True)
                        state.load_board()
                        state.pos_moves()

    return winning_board, states
