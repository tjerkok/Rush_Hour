# Rush Hour

### Submission requirements README
* Introduction to case
* Description of approach to the algorithms 
* After reading this it is clear how...
    * the results can be reproducted 
    * what cmd line arguments are possible for multiple functionalities/algorithms
    * to obtain a certain result via a certain file

## Rush Hour case explanation
Rush Hour seems to be an easy puzzle, altough it has a surprising challenging character. In a square field with varying dimensions is a black car named 'X', your car. This car must go to the exit, which is placed right in front of the car. However, other vehicles, cars of two units and trucs of three units, that may only be moved in their direction of travel, block the way to the exit. The vehicles are not aloud to turn around. The assignment is simple: clear the way to the exit by moving other vehicles and move your black car to the exit. 

## Requirements
Dependencies in 'requirements.txt'.
* numpy==1.19.4
* matplotlib==3.3.3

## Usage
python3 main.py [gameboards/"gamename".csv] ["algorithm"] (["heuristic"]) (["sample size"]) (["max depth"])

* If no algorithm is given, you play the game yourself.
* Choose heuristic between H1 and H9. 
* Give sample size if using the "Random" algorithm.
* Give max depth if using the IDDFS (required).

Algorithms: 
* "Random": Random search
* "BFS" : Breadth-First search
* "BFS_beam": Breadth-First search with beam 
* "BFS_priority": Breadth-First search with priority queue
* "IDDFS": Iterative Deepenening Depth-First search

Heuristics: 
* H1: maximal number of free spaces ahead of the target car
* H2: minimum number of vehicles blocking the target car
* H3: minimum distance to the goal position for the target car
* H4: H2 + H3 
* H5: H2 + H3 + H8
* H6: H2 + H8
* H7: most possible moves per state 
* H8: minimum number of blocked blocking vehicles
* H9: minimum number of required moves

## Results and output 
* output/output.csv: saves for every vehicle the move that it has made per run in chronological order. 
* output/log.csv: logbook that saves per run per filename the algorithm used, the amount of moves performed, the amount of states checked and the time that has been passed. 
* output/startboard.png: a visualisation of the game's startboard. 
* output/endboard.png: a visualisation of the game's winning endboard.

## Structure
* /code
    * /algorithms: multiple algorithms to play the game.
    * /classes: two classes for this game: Board and Vehicle.
    * /visualization: code for matplot visualization of the gameboard. 
    * /input/output: two functions for loading input and generating output. 
* /gameboards: csv input with multiple gameboards. 
* /output: csf output with the moves per vehicle to come to a win.
* /docs: contains the design document. 
* /statespace: contains calculations of the state space assignment. 

## Authors
* Tjerko Kieft
* Bob Nieuwenhuize
* Kika Banning