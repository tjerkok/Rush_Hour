#############################################################
# visualization.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Creates a visualization of the board and saves the image.
#############################################################

import matplotlib.pyplot as plt
import numpy as np
from string import ascii_uppercase


def visualize(board, state):
    """Creates a visualisation of the gameboard using matplotlib."""
    # checks if the board is a numpy array
    if not isinstance(board, np.ndarray):
        return False

    # closes startboard
    if state == "end":
        plt.close()

    legend = {}
    i = 0
    image = []

    # giving vehicle names values
    for letter in ascii_uppercase:
        if len(board[0]) >= 10:
            letter = letter + ' '

        if letter in ('X', 'X '):
            legend['X'] = -1
        else:
            legend[letter] = i
            i += 1

    # giving values to double letter names
    for letter in ascii_uppercase:
        legend['A' + letter] = i
        i += 1

    # creates an image array with the values instead of names
    for element in board:
        element = [legend[letter] if letter in legend else 0 for letter in element]
        image.append(element)

    image = np.array(image)

    # sets layout for image
    plt.imshow(image, cmap='hot_r', interpolation='nearest')
    ax = plt.gca()
    ax.set_xticks([], minor=False)
    ax.set_yticks([], minor=False)
    ax.set_xticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.tick_params(axis=u'both', which=u'both', length=0)
    ax.set_xticklabels([])

    # defines colours for vehicles
    for i in range(np.size(board, 0)):
        for j in range(np.size(board, 1)):
            if board[i, j] == 'X' or board[i, j] == 'X ':
                ax.text(j, i, board[i, j], ha='center',
                        va='center', color='blue')
            elif image[i, j] <= np.amax(image)/2:
                ax.text(j, i, board[i, j], ha='center',
                        va='center', color='black')
            elif image[i, j] > np.amax(image)/2:
                ax.text(j, i, board[i, j], ha='center',
                        va='center', color='white')
            else:
                ax.text(j, i, board[i, j], ha='center',
                        va='center', color='black')

    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    # saves visualization
    plt.savefig(f'output/{state}board.png', dpi=400)

    return True
