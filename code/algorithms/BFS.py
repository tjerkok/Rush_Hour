####################################################################
# BFS.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Class with Breadth First Search algorithm for Rush Hour game.
#####################################################################

from .priority import Priority
import copy

class BFS:
    """
    A class that uses the Breadth First Search Algorithm.

    Attributes:
    board: Board object. 
    boardsize: int with boardwidth.
    vehicle_length: int with vehicle length.
    states: list with all possible states.
    boards_visited: set with all hashed visited boards.
    winning_board: Board object with vehicles orientated in winning position.
    state_space: int that counts the amount of states checked.
    beam: bool for beam search.
    priority: bool for priority queue search.
    heuristic: str with the input heuristic.
    lookahead: bool for lookahead.
    move: int that counts the amount of moves within a depth.
    apply_priority: int from which depth priority is applied.

    Methods:
    get_next_state: picks the first item from the list with states.
    build_children: creates all possible child-states from the current state
    and adds them to the archive.
    add_to_archive: checks if a state is already visited.
    combine_algorithm: applies priority, with or without beam search to BFS.
    run: runs the algorithm until all states are checked or untill won. 
    """

    def __init__(self, board, beam=False, priority=False, heuristic='H1', lookahead=True):
        """Loads all information neccessary for the BFS."""
        self.board = copy.deepcopy(board)
        self.boardsize = board.boardsize
        self.vehicle_length = len(board.vehicles)
        self.states = [copy.deepcopy(self.board)]
        self.boards_visited = set()
        self.winning_board = None
        self.state_space = 1
        self.beam = beam
        self.priority = priority
        self.heuristic = heuristic
        self.lookahead = lookahead
        self.move = 0
        self.apply_priority = 0

    def get_next_state(self):
        """Gets the next state from the list of states."""
        return self.states.pop(0)

    def build_children(self, board):
        """Creates all possible child-states."""
        for vehicle, movelist in board.pos_moves().items():
            for vehicle_move in movelist:
                child = copy.deepcopy(board)
                if not child.move(vehicle, vehicle_move):
                    print("invalid move")
                    return False

                if child.win() and self.lookahead:
                    self.winning_board = child
                    return True

                self.add_to_archive(child)

        return False

    def add_to_archive(self, board):
        """Function that adds the checked states to the archive."""
        board_array = board.load_board()

        # makes np array immutable and hashes it
        board_array.flags.writeable = False
        hashed_board = hash(board_array.tostring())

        # checks if hashed board is already checked for win
        if hashed_board not in self.boards_visited:
            self.boards_visited.add(hashed_board)
            self.states.append(board)
            self.state_space += 1

    def run(self):
        """Runs the algorithm untill all possible states are checked."""
        while self.states:

            new_board = self.get_next_state()

            # checks for moves left, beam and priority
            if self.move < len(new_board.moves) and (
                self.priority or self.beam):
                self.states = Priority(
                            self.states,
                            len(self.states),
                            self.boardsize,
                            self.vehicle_length,
                            self.heuristic,
                            self.beam)
                self.move = len(new_board.moves)

            # check for win
            if new_board.win():
                self.winning_board = new_board
                return self.winning_board, self.state_space

            # build children
            elif self.build_children(new_board):
                return self.winning_board, self.state_space

        # if list with states empty but not won, return None board
        return None, self.state_space
