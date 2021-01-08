#########################################################
# shortest_winning_testboard.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwehuizen, Kika Banning 
# 
# Testfunction.
#########################################################

def winning_moves(board):

    print(board.load_board())
    moves = []
    winning_moves_tuple = [['F', -3], ['B', -3], ['A', 1], ['C', 1], ['E', 1], ['G', -2], ['D', -2], ['X', 3]]

    while not board.win():
        for winning_move in winning_moves_tuple:
            board.pos_moves()

            vehicle_name = winning_move[0]
            shift = winning_move[1]
            moves.append([vehicle_name, int(shift)])

            if board.move(vehicle_name, int(shift)):
                print(board.load_board())

    if board.win():
        print('game won')

    return moves
