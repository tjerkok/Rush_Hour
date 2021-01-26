#########################################################
# generate_output.py
#
# Programmeertheorie, Rush Hour
# Tjerko Kieft, Bob Nieuwenhuize, Kika Banning
#
# Generates log output in a csv file
#########################################################

import csv

def summary(filename, algorithm, amount_of_moves, states, time):
    """Generates a log csv file with the algorithms done"""
    with open('output/log.csv', 'a', newline='') as csvfile:
        newline = csv.writer(csvfile, delimiter=',')
        row = [filename, algorithm, amount_of_moves, states, time]
        newline.writerow(row)
