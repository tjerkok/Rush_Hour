#########################################################
# main.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Plays the Rush Hour game, using different algorithms.
#########################################################

from code.algorithms import randomise, play_yourself, shortest_winning_testboard
from code.visualization.visualization import visualize
from code.input.output.load_in import load_problem
from code.input.output.generate_output import output
from sys import argv

if __name__ == '__main__':

    # ------------------------------ Input ------------------------------
    if len(argv) == 2:
        filename = argv[1]
    else:
        print('Usage: python3 main.py [gameboards/Rushhour9x9_4.csv]')
        exit(1)

    board = load_problem(filename)
    if not visualize(board.load_board(), 'start'):   # result in code/visualization/test.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    # -------------------------- Random choice --------------------------

    moves = randomise.random_moves_algorithm(board)

    if not visualize(board.load_board(), 'end'):   # result in code/visualization/test.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    moves_needed = len(moves)
    print(moves_needed)

    # -------------------------- Play yourself --------------------------

    #moves = play_yourself.play(board)

    # ----------- Shortest Winning game testboard (hardcoded) -----------

    #moves = shortest_winning_testboard.winning_moves(board)

    #moves_needed = len(moves)
    #print(moves_needed)

    # ----------------------------- Output ------------------------------

    output = output(moves)
