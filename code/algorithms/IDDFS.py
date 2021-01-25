###############################################################
# IDDFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# A Depth First Search algorithm and an Iterative Deepening Depth
# First Search algorithm.
###############################################################

from .BFS import BFS


class DFS(BFS):
    """Class to use the Depth First Search on a Board object."""
    def __init__(self, board, max_depth=10000):
        """ Depth First Search is based on the Breadth First Search
            class, so it takes the same attributes, but turned
            lookahead off. The archive boards_visited is a dictionary
            to keep track of the depth of the visited board. """
        BFS.__init__(self, board, lookahead=False)
        self.max_depth = max_depth
        self.boards_visited = {}
        self.state_space = 0

    def get_next_state(self):
        """Returns the last element from the list. This way it functions
        as a stack instead of a queue (BFS)."""
        return self.states.pop()

    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()
        board_array.flags.writeable = False
        hashed_board = hash(board_array.tostring())

        # check if the hashed board is already known
        if hashed_board in self.boards_visited:
            # checks if board is found after less moves, add to stack
            if self.boards_visited[hashed_board] > len(board.moves):
                self.boards_visited[hashed_board] = len(board.moves)
                self.states.append(board)
                self.state_space += 1
        else:
            self.boards_visited[hashed_board] = len(board.moves)
            self.states.append(board)

    def run(self):
        """Runs the algorithm until the stack is empty or when a
        winning board is found."""
        while self.states:
            new_board = self.get_next_state()
            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space
            # don't make children when max depth is reached
            elif len(new_board.moves) < self.max_depth:
                # build.children returns True when lookahead finds win
                if self.build_children(new_board): 
                    return self.winning_board, self.state_space

        return None, self.state_space


class IDDFS:
    """Class to use the Iterative Deepening Depth First Search on a 
    Board object with a maxdepth."""
    def __init__(self, board, max_depth):
        self.max_depth = max_depth
        self.board = board
        self.winning_board = None
        self.boards_visited = set()
        self.state_space = 0

    def run(self):
        """Runs the algorithm. For every depth until the max depth a
        DFS object is made and runs."""
        # derives the mninimum amount of moves
        minimum = self.board.MinMovesHeuristic()
        print(f"minimum moves required: {minimum}")

        # starts at the minimum amount of moves (depth) until max depth
        for depth in range(minimum, self.max_depth + 1):
            print(f"depth: {depth}")
            depth_first = DFS(self.board, depth)
            self.winning_board, states = depth_first.run()
            # saves the states from one DFS to the total amount of states
            self.state_space += states
            # if True, a winning board is found
            if self.winning_board is not None:
                return self.winning_board, self.state_space
        # if winning board is still None, no solution has been found
        return self.winning_board, self.state_space
