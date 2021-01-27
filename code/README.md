# Code explanation
This folder contains all the code that is used by the main.py 

## Structure
* /algorithms: contains all different algorithms to play the game with.
    * BFS.py: Breadth First Search.
    * biggest_step.py: BFS with heuristic for biggest step first. 
    * IDDFS.py: Iterative Deepening Depth First Search.
    * play_yourself.py: play the Rush Hour game yourself.
    * priority.py: uses Priority queue search and Beam search with multiple heuristics.
    * randomise.py: uses Random algorithm. 
* /classes: contains two classes for the objects Board and Vehicle. 
    * board.py: Class Board
    * vehicle.py: Class Vehicle
* /input_output: contains functions for loading input and generating output. 
    * generate_output.py: generates output.csv with all moves per vehicle. 
    * load_in.py: loads gameboards in. 
    * summary.py: logbook that keeps track of all games in log.csv: filename, algorithm, amount of moves, states, time.
    * visualization.py: generates png of startboard and endboard. 

