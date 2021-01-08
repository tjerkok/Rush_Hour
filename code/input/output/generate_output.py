import csv


def output(moves):
    with open('output/output.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['car', 'move'])
        for move in moves:
            w.writerow(move)
    return w
