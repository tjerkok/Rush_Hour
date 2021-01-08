#########################################################
# play_yourself.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwehuizen, Kika Banning 
# 
# Function to play the Rush Hour game yourself.  
#########################################################

def play(board):
    """Function to play the Rush Hour game yourself with your keyboard.""" 
    print(board.load_board())
    moves = []
    counter = 0
    max_moves = 30

    while not board.win() and counter < max_moves:
        
        # User input for move
        vehicle_name = input('letter of the vehicle you want to move: ').upper()
        shift = input('places to move that vehicle, use minus for left/down: ')
        board.pos_moves()

        # Vehicle moves if possible
        if board.move(vehicle_name, int(shift)):
            print(board.load_board())
            moves.append([vehicle_name, int(shift)])
            counter += 1
        else:
            print('not allowed')

    if board.win():
        print('game won')

    elif counter == max_moves:
        print('maximum moves reached')

    return moves
