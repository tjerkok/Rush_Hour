#########################################################
# main.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Plays the Rush Hour game, using different algorithms.
# Algorithms to choose: Random or BFS.
# If no algorithm chosen then you can play the game yourself.
#########################################################

from code.algorithms import randomise, play_yourself, BFS
from code.visualization.visualization import visualize
from code.input.output.load_in import load_problem
from code.input.output.generate_output import output
from code.input.output.summary import summary
from sys import argv
import time

if __name__ == '__main__':

    # ------------------------------ Input ------------------------------

    if len(argv) == 3:
        filename = argv[1]
        algorithm = argv[2]
    elif len(argv) == 2:
        filename = argv[1]
        algorithm = 'None'
    else:
        print('Usage: python3 main.py [gameboards/Rushhour9x9_4.csv] [algorithm]')
        exit(1)

    board = load_problem(filename)

    if not visualize(board.load_board(), 'start'):   # result in code/visualization/test.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    time0 = time.time()

    # -------------------------- Random choice --------------------------

    if algorithm == 'Random':
        winning_board = randomise.random_moves_algorithm(board)

            
        states = 'None'

    # -------------------------- Play yourself --------------------------

    elif algorithm == 'None':
        winning_board = play_yourself.play(board)

    # ----------------------- Breadth First Search ----------------------

    elif algorithm == 'BFS':
        winning_board, states = BFS.BFS(board)


    # ----------------------------- Output ------------------------------

    if not visualize(winning_board.load_board(), 'end'):   # result in code/visualization/test.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    #output = output(moves)
    time1 = time.time() - time0
    print("winning")
    print(winning_board.load_board())
    print(f"states: {states}")
    print(f"moves: {winning_board.moves}")
    print(f"amount of moves: {len(winning_board.moves)}")
    summary(filename, algorithm, len(winning_board.moves), states, round(time1, 4))
