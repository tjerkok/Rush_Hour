#########################################################
# main.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Plays the Rush Hour game, using different algorithms.
# Algorithms to choose: Random, BFS or BFS_beam.
# If no algorithm chosen then you can play the game yourself.
#########################################################

from code.algorithms import randomise, play_yourself, BFS
from code.visualization.visualization import visualize
from code.input.output.load_in import load_problem
from code.input.output.generate_output import output
from code.input.output.summary import summary
from sys import argv, getsizeof
import time


if __name__ == '__main__':

    # ------------------------------ Input ------------------------------

    if len(argv) == 3:
        filename = argv[1]
        algorithm = argv[2]
        if algorithm == 'Random':
            sample_size = 1
    elif len(argv) == 4 and argv[2] == 'Random':
        filename = argv[1]
        algorithm = argv[2]
        sample_size = int(argv[3])
    elif len(argv) == 2:
        filename = argv[1]
        algorithm = 'None'
    else:
        print('Usage: python3 main.py [gameboards/Rushhour9x9_4.csv] [algorithm] ([sample size])')
        exit(1)

    board = load_problem(filename)
    start_board = board.load_board()

    if not visualize(start_board, 'start'):   # result in code/visualization/startboard.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    time0 = time.time()

    # -------------------------- Random choice --------------------------

    if algorithm == 'Random':

        winning_board, amount_of_moves, time1 = randomise.random_moves_algorithm(filename, sample_size)

        if sample_size > 1:
            average_amount_of_moves = sum(amount_of_moves) / sample_size
            average_time_elapsed = sum(time1) / sample_size

            print(f"amount of moves min: {min(amount_of_moves)}")
            print(f"amount of moves max: {max(amount_of_moves)}")
            print(f"amount of moves average: {average_amount_of_moves}")
            print(f"amount of time average: {average_time_elapsed}")
        else:   # misschien deze else statement laten zitten omdat dat onderaan ook al weergegeven wordt
            print(f"amount of moves: {amount_of_moves[0]}")
            print(f"time elapsed: {time1[0]}")

        states = 'None'

    # -------------------------- Play yourself --------------------------

    elif algorithm == 'None':

        winning_board = play_yourself.play(board)

    # ----------------------- Breadth First Search ----------------------

    elif algorithm == 'BFS':
        winning_board, states = BFS.BFS(board, False, False)
        
    elif algorithm == 'BFS_beam':
        winning_board, states = BFS.BFS(board, True, False)

    elif algorithm == 'BFS_priority':
        winning_board, states = BFS.BFS(board, False, True)
   

    else:
        print("Algorithm doesn't exist")
        exit()

    # ----------------------------- Output ------------------------------
    time1 = time.time() - time0

    if not visualize(winning_board.load_board(), 'end'):   # result in code/visualization/endboard.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    # serial = winning_board.serialize()
    # print(serial)
    # unserial = winning_board.unserialize(serial)
    # print(unserial)
    # winning = winning_board.load_board()
    # winning.flags.writeable = False
    # hashed_winning = hash(winning.tostring())
    # print(f"size of hashed winning array: {getsizeof(hashed_winning)}")
    # print(f"size of winning array: {getsizeof(winning)}")
    # print(f"size of winning board: {getsizeof(winning_board)}")
    # print(f"size of {type(unserial)} unserialized board: {getsizeof(unserial)}")
    # print(f"size of serialized board: {getsizeof(serial)}")
    # print(f"size of np array to bytes: {getsizeof(winning.tobytes())}")

    output = output(winning_board.moves)

    print(start_board)
    print("game won")
    print(winning_board.load_board())
    print(f"states: {states}")
    print(f"moves: {winning_board.moves}")
    print(f"amount of moves: {len(winning_board.moves)}")
    summary(filename, algorithm, len(winning_board.moves), states, round(time1, 4))
