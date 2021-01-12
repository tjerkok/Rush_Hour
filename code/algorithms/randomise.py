###############################################################
# randomise.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function with randomise algorithm to play the Rush Hour game.
###############################################################

import random


def random_moves_algorithm(board):
    """Function that plays the Rush Hour game with a randomise algorithm."""

    print(board.load_board())

    while not board.win():
        # Lists all possible moves and picks one random
        possible_moves = list(board.pos_moves().items())
        rand = random.choice(possible_moves)

        # Moves vehicle if possible, else picks new random move
        if rand[1] != []:
            vehicle_name = rand[0]
            possible_shifts = rand[1]
            shift = random.choice(possible_shifts)

            board.move(vehicle_name, int(shift))
            print(board.load_board())

    if board.win():
        winning_board = board

    return winning_board
