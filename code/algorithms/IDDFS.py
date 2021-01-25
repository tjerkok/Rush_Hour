###############################################################
# IDDFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# A Depth First Search algorithm and an Iterative Deepening Depth
# First Search algorithm.
###############################################################

# anytree: https://pypi.org/project/anytree/
import copy
import time
from .BFS import BFS


class DFS(BFS):
    def __init__(self, board, max_depth=10000):
        BFS.__init__(self, board, lookahead=False)
        self.max_depth = max_depth
        self.boards_visited = {}
        self.state_space = 0

    def get_next_state(self):
        return self.states.pop()

    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()
        board_array.flags.writeable = False
        hashed_board = hash(board_array.tostring())

        if hashed_board in self.boards_visited:
            if self.boards_visited[hashed_board] > len(board.moves):
                self.boards_visited[hashed_board] = len(board.moves)
                self.states.append(board)
                self.state_space += 1
        else:
            self.boards_visited[hashed_board] = len(board.moves)
            self.states.append(board)

    def run(self):
        """Runs the algorithm until all possible states are checked."""

        while self.states:
            new_board = self.get_next_state()
            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space
            else:
                if True:
                    print(f"moves done in this state: {new_board.moves}")
                    print("possible moves")
                    print(new_board.load_board())
                    print("pos moves")
                    print(new_board.pos_moves())

                if len(new_board.moves) < self.max_depth:
                    if self.build_children(new_board): # lijst vullen met kids, return True bij child.win()
                        return self.winning_board, self.state_space

                if False:
                    print(len(self.states))
                    print([f"{a.moves[0:2]}" for a in self.states])

        return None, self.state_space


class IDDFS:
    def __init__(self, board, max_depth):
        self.max_depth = max_depth
        self.board = board
        self.winning_board = None
        self.boards_visited = set()
        self.state_space = 0

    def run(self):
        minimum = self.board.MinMovesHeuristic()
        print(f"minimum moves required: {minimum}")
 
        for depth in range(minimum, self.max_depth + 1):
            print(f"depth: {depth}")
            depth_first = DFS(self.board, depth)
            winning_board, states = depth_first.run()
            self.state_space += states
            if winning_board is not None:
                return winning_board, self.state_space

        return winning_board, self.state_space
