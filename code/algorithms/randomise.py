###############################################################
# randomise.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Function with randomise algorithm to play the Rush Hour game.
###############################################################

import random
import time
import csv
from ..input.output.load_in import load_problem


def random_moves_algorithm(filename, sample_size):
    """Function that plays the Rush Hour game with a randomise algorithm."""

    amount_of_moves = []
    time1 = []
    min_moves = 1000000

    for i in range(sample_size):
        board = load_problem(filename)
        time0 = time.time()
        board.load_board()

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
                board.load_board()

        if board.win():
            winning_board = board
            # print(winning_board.load_board())

            if len(winning_board.moves) < min_moves:
                lowest_moves_board = winning_board
                min_moves = len(winning_board.moves)

        time1.append(time.time() - time0)
        amount_of_moves.append(len(winning_board.moves))
        if sample_size > 1:
            print(f"boards won: {i + 1}")

    with open('output/baseline.csv', 'a', newline='') as csvfile:
        a = csv.writer(csvfile, delimiter=',')
        a.writerow([filename, amount_of_moves])
        a.writerows(map(lambda x: [x], amount_of_moves))

    return lowest_moves_board, amount_of_moves, time1
