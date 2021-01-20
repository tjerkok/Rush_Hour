###############################################################
# IDDFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# TODO.
###############################################################

# anytree: https://pypi.org/project/anytree/
import copy
import time
from .BFS import BFS


class DFS(BFS):
    def __init__(self, board, max_depth=10000):
        BFS.__init__(self, board)
        self.max_depth = max_depth
        self.boards_visited = {}

    def get_next_state(self):
        return self.states.pop()

    # erg sloom (!!!)
    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()
        board_array.flags.writeable = False
        hashed_board = hash(board_array.tostring())
        
        if hashed_board in self.boards_visited:
            if self.boards_visited[hashed_board] > len(board.moves):
                self.boards_visited[hashed_board] = len(board.moves)
                self.states.append(board)
        else:
            self.boards_visited[hashed_board] = len(board.moves)
            self.states.append(board)

    def run(self):
        """Runs the algorithm until all possible states are checked."""

        while self.states != []:
            new_board = self.get_next_state()
            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space
            else: 
                if False:
                    print(f"moves done in this state: {new_board.moves}")
                    print("possible moves")
                    print(new_board.load_board())
                    print(new_board.pos_moves())

                if len(new_board.moves) < self.max_depth:
                    self.build_children(new_board) # lijst vullen met kids


                if False:
                    print(len(self.states))
                    print([f"{a.moves[0:2]}" for a in self.states])

        return None, self.state_space

# moves: [['A', 1], ['C', -1], ['E', -1], ['F', -3], ['B', 3], ['G', -2], ['D', 2], ['X', 3]]

class IDDFS:
    def __init__(self, board, max_depth):
        self.max_depth = max_depth
        self.board = board
        self.winning_board = None
        self.boards_visited = set()

    def run(self):
        for depth in range(1, self.max_depth):
            print(f"depth: {depth}")
            depth_first = DFS(self.board, depth)
            winning_board, states = depth_first.run()
            if winning_board is not None:
                return winning_board, states

        return winning_board, states
