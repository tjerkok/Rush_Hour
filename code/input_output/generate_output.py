#######################################################
# generate_output.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Generates output in a csv file: output/output.csv
# the output includes all performed moves.
#######################################################

import csv


def output(moves):
    """Generates an output csv file with all moves per car"""

    with open('output/output.csv', 'w', newline='') as csvfile:
        output = csv.writer(csvfile, delimiter=',')
        output.writerow(['car', 'move'])
        for move in moves:
            output.writerow(move)
    return output
