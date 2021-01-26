#########################################################
# main.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Plays the Rush Hour game, using different algorithms.
# Algorithms to choose: Random, BFS, BFS_beam, BFS_priority and IDDFS
# If no algorithm chosen then you can play the game yourself.
# Heuristics to choose: H1 t/m H9. If none is chosen, H1 will be
# selected.
#########################################################

from code.algorithms import randomise, play_yourself, BFS, IDDFS, biggest_step
from code.input_output.visualization import visualize
from code.input_output.load_in import load_problem
from code.input_output.generate_output import output
from code.input_output.summary import summary
from sys import argv
import time


def No_solution():
    """Returns error when no solution has been found."""

    print("The winning board was not found. Try increasing the max depth"
          " when using the IDDFS algorithm.")
    exit()

def Wrong_usage():
    """Returns error when the usage is wrong."""

    print("Usage: python3 main.py [gameboards/Rushhour9x9_4.csv] [algorithm]"
    " ([sample size]) ([heuristic]) ([max_depth])")
    print('Give no algorithm input to play by yourself.\nAlgorithms: \n-Random\n-BFS\n-BFS_beam\n-BFS_priority\n-BFS_step\n'
    '-IDDFS\nHeuristics: H1 t/m H9\nRandom:\n-sample size\nIDDFS:\n-max_depth (required)')
    exit(1)


if __name__ == '__main__':

    # ------------------------------ Input ------------------------------
    # handles the various combinations of input
    if 1 <= len(argv) <= 4:
        filename = argv[1]
        if len(argv) >= 3:
            algorithm = argv[2]
            if algorithm == 'Random':
                if len(argv) == 4:
                    if not argv[3].isnumeric():
                        Wrong_usage()
                    sample_size = int(argv[3])
                else:
                    sample_size = 1

            elif len(argv) == 4:
                if algorithm == 'IDDFS':
                    max_depth = int(argv[3])
                else:
                    heuristic = argv[3]
            else:
                heuristic = 'H1'
        else:
            algorithm = 'None'
    else:
        Wrong_usage()

    # loads the csv file and creates the vehicles and board
    board = load_problem(filename)

    # visualizes the starting board, if failed the error is displayed
    if not visualize(board.load_board(), 'start'):   # result in code/visualization/startboard.png
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    # keeps track of the time the algorithm takes
    time0 = time.time()

    # -------------------------- Random choice --------------------------

    if algorithm == 'Random':
        # runs the random algorithm with given sample size
        winning_board, amount_of_moves, time1 = randomise.random_moves_algorithm(
            board, sample_size, filename)

        # calculates averages of results
        if sample_size > 1:
            average_amount_of_moves = sum(amount_of_moves) / sample_size
            average_time_elapsed = sum(time1) / sample_size

            print(f"amount of moves min: {min(amount_of_moves)}")
            print(f"amount of moves max: {max(amount_of_moves)}")
            print(f"amount of moves average: {average_amount_of_moves}")
            print(f"amount of time average: {average_time_elapsed}")
        # saves values for end results if random ran once
        else:
            amount_of_moves = [amount_of_moves[0]]
            time1 = [time1[0]]

    # -------------------------- Play yourself --------------------------

    elif algorithm == 'None':
        winning_board = play_yourself.play(board)

    # ----------------------- Breadth First Search ----------------------

    # runs the BFS with/without beam and/or priority
    elif algorithm[0:3] == 'BFS':
        if algorithm == 'BFS' and len(argv) == 3:
            breadth_first = BFS.BFS(board, False, False)
            winning_board, states = breadth_first.run()
        elif algorithm == 'BFS_beam':
            breadth_first = BFS.BFS(board, True, False, heuristic)
            winning_board, states = breadth_first.run()
            algorithm = f"{algorithm} {heuristic}"
        elif algorithm == 'BFS_priority':
            breadth_first = BFS.BFS(board, False, True, heuristic)
            winning_board, states = breadth_first.run()
            algorithm = f"{algorithm} {heuristic}"
        elif algorithm == 'BFS_step':
            step = biggest_step.Step(board)
            winning_board, states = step.run()
        else:
            Wrong_usage()

    # --------------------- Depth First Search --------------------------

    # runs Depth First Search
    elif algorithm == 'DFS':
        depth_first = IDDFS.DFS(board)
        winning_board, states = depth_first.run()

    # ------------- Iterative Deepening Depth First Search --------------

    # Runs the Iterative Deepening Depth First Search
    elif algorithm == 'IDDFS':
        i_depth_first = IDDFS.IDDFS(board, max_depth)
        winning_board, states = i_depth_first.run()

    # ------------------------------- Wrong input -----------------------

    # If the algorithm input didn't match any of the known algorithms
    else:
        print("Algorithm doesn't exist")
        Wrong_usage()

    # ----------------------------- Output ------------------------------
    # No solution has been found
    if winning_board is None:
        No_solution()

    # save time and moves values to print
    if algorithm != 'Random':
        time1 = time.time() - time0
        amount_of_moves = len(winning_board.moves)

    # result in code/visualization/endboard.png
    if not visualize(winning_board.load_board(), 'end'):
        print("Could not visualize board as board is not of type numpy.ndarry")
        exit()

    # prints results
    print("start board:")
    print(board.load_board())
    print("end board")
    print(winning_board.load_board())
    if algorithm == 'Random':
        states = sum(amount_of_moves) + 1
        time1 = sum(time1)
    elif algorithm == 'None':
        states = amount_of_moves + 1
    else:
        print(f"amount of moves: {amount_of_moves}")
    print(f"time elapsed: {time1}")
    print(f"states: {states}")
    print(f"moves: {winning_board.moves}")

    # saves run to the log and generates output
    summary(filename, algorithm, len(winning_board.moves), states, round(time1, 4))
    output = output(winning_board.moves)
