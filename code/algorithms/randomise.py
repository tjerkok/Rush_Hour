import random


def random_moves_algorithm(board):

    print(board.load_board())
    moves = []
    counter = 0

    while not board.win():
        possible_moves = list(board.pos_moves().items())

        rand = random.choice(possible_moves)

        if rand[1] != []:
            vehicle_name = rand[0]
            possible_shifts = rand[1]
            shift = random.choice(possible_shifts)

            board.move(vehicle_name, int(shift))
            print(board.load_board())

            moves.append([vehicle_name, int(shift)])
            counter += 1

    if board.win():
        print('game won')

    return moves
