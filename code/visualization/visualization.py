#############################################################
# visualization.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Creates a visualization of the board and saves the images.
#############################################################

from string import ascii_uppercase
import matplotlib.pyplot as plt
import numpy as np

def visualize(board, state):
    """Creates a visualisation of the gameboard using matplotlib"""

    # checks if the board is a numpy array
    if not isinstance(board, np.ndarray):
        print("board is not a numpy array")
        return False

    plt.close()
    legend = {}
    i = 0
    image = []

    # Vehicle names
    for letter in ascii_uppercase:
        if len(board[0]) >= 10:
            letter = letter + ' '

        if letter == 'X' or letter == 'X ':
            legend['X'] = -1

        else:
            legend[letter] = i
            i += 1

    for letter in ascii_uppercase:
        legend['A'+letter] = i
        i += 1

    for element in board:
        element = [legend[letter] if letter in legend else 0 for letter in element]
        image.append(element)

    image = np.array(image)

    # Sets layout for image
    plt.imshow(image, cmap='hot_r', interpolation='nearest')
    ax = plt.gca()
    ax.set_xticks([], minor=False)
    ax.set_yticks([], minor=False)
    ax.set_xticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.tick_params(axis=u'both', which=u'both',length=0)
    ax.set_xticklabels([])

    # Defines colours for vehicles
    for i in range(np.size(board, 0)):
        for j in range(np.size(board, 1)):
            if board[i, j] =='X' or board[i, j] == 'X ':
                ax.text(j, i, board[i, j], ha='center', va='center', color='blue')
            elif image[i, j] <= np.amax(image)/2:
                ax.text(j, i, board[i, j], ha='center', va='center', color='black')
            elif image[i, j] > np.amax(image)/2:
                ax.text(j, i, board[i, j], ha='center', va='center', color='white')
            else:
                ax.text(j, i, board[i, j], ha='center', va='center', color='black')

    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    # Saves visualization
    plt.savefig(f'code/visualization/{state}board.png', dpi=400)

    return True
