#########################################################
# generate_output.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Generates output in a csv file
#########################################################

import csv


def output(moves):
    """Generates an output csv file with all moves per car"""

    with open('output/output.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['car', 'move'])
        for move in moves:
            w.writerow(move)
    return w
