# function to create a visualization and save the images
from string import ascii_uppercase
import matplotlib.pyplot as plt
import numpy as np

def visualize(board):
    legend = {}
    i = 0
    image = []

    for letter in ascii_uppercase:
        legend[letter] = i
        i += 1

    for element in board:
        element = [legend[letter] if letter in legend else 0 for letter in element]
        image.append(element)

    image = np.array(image)

    plt.imshow(image, cmap='hot_r', interpolation='nearest')
    ax = plt.gca()
    ax.set_xticks([], minor=False)
    ax.set_yticks([], minor=False)
    ax.set_xticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(board[0]), 1), minor=True)
    ax.tick_params(axis=u'both', which=u'both',length=0)
    ax.set_xticklabels([])
    
    for i in range(len(board[0])):
        for j in range(len(board[1])):
            if board[i, j] =='X':
                ax.text(j, i, board[i, j], ha="center", va="center", color="white")
            elif board[i, j] != '_':
                ax.text(j, i, board[i, j], ha="center", va="center", color="black")

    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    plt.savefig('code/visualization/test.png', dpi=400)
