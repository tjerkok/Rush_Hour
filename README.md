# Rush Hour

## Rush Hour 
Rush hour is a puzzle where the goal is to lead the red (target) car to the exit, right in front of it. However, there are other vehicles that block the road, cars of two units long and trucks three units long. Each vehicle can only move forward and backward in the direction of its position (horizontal/vertical). The task here is therefore to clear the way to the exit by moving vehicles and bringing the red (target) car to the exit. 

## Description of approach to the algorithms
* Random: a random vehicle is first selected from the list of all possible vehicles that can move. A random move is then selected from all possible moves for that vehicle.
* Breadth First Search(BFS): for each state of the board all possible moves are performed and the new required states of the board are then added to the queue (FIFO) with all states. 
    * Archive: the archive keeps track of which state is already in the archive, if the state is already in the archive, no new children are being build and the state is not added to the queue. 
    * Beam + heuristics: We give the queue to our Beam function, which is then sorted based on heuristics and the 'worst' states are cut off from the queue. 
        * Beam ratio vs width: At first we had the idea that it was best to cut a percentage of the queue length, called a beam ratio. This only entails risks, because in Rush Hour it is sometimes the case that you have to go back one step and then go forward two. The risk of this is therefore that youcut away the optimal solution too quickly. After this we found that 80% of the random puzzles with a 7x7 board are solved with a Beam width of 10000. We therefore use the following formula for the beam width: (board size ^ 2) / (7 ^ 2) * 10000. 
    * Priority + heuristics: the priority queue does basically the same as the beam search. However, the worst states are not cut off.
    * Early solution detection (lookahead): Early solution detection is applied at the moment that children are created in the BFS. If a child already solves the board, the solution is immediately returned, instead of first creating all other children. 
    * Biggest step heuristic: from the list of possible moves per vehicle is only the biggest step possible moved for every vehicle. 
* Iterative Deepening Depth First Search algoritme(IDDFS): this is actually a Depth First Search(DFS) which continuously increases its depth one step until a solution is found. This means that the algorithm starts at the beginning state, and then searches all possible states to a certain depth. The disadvantage of the IDDFS is that it takes a lot of time to come to a solution, so where for BFS the problem is memory, with IDDFS this is the time. The reason for this is that the entire search tree has to be run again with DFS when increasing the depth by one. That means a lot of unnecessary work. 
    * Heuristic: to speed up the process of the IDDFS, we have used a heuristic that calculates the minimum number of required moves and only starts searching from that depth. 

## Requirements
This codebase is fully written in Python 3.8.5 until 3.9.1. 
The packages for running this code are in requirements.txt and can be installed using pip: "pip install -r requirements.txt"
* numpy, versie 1.19.4
* matplotlib, versie 3.3.3

## Usage
python3 main.py [gameboards/"gamename".csv] (["algorithm"]) (["heuristic"]) (["sample size"]) (["max depth"])

* If no algorithm is given, you play the game yourself.
* Give sample size if using the "Random" algorithm.
* Give max depth if using the IDDFS (required).

Algorithms: 
* "Random": Random search
* "BFS" : Breadth-First search
* "BFS_beam": Breadth-First search with beam 
* "BFS_priority": Breadth-First search with priority queue
* "BFS_step": Breadth-First search where the biggest steps of all cars is done first.
* "BFS_step_beam": Breadth-First search with beam and biggest step.
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
* output/log.csv: logbook that saves per run the filename, the algorithm used, the amount of moves performed, the amount of states checked and the time that has been passed. 
* output/startboard.png: a visualisation of the game's startboard. 
* output/endboard.png: a visualisation of the game's winning endboard.

## Structure
* /code
    * /algorithms: multiple algorithms to play the game.
    * /classes: two classes for this game: Board and Vehicle.
    * /visualization: code for matplot visualization of the gameboard. 
    * /input_output: functions for loading input and generating output, log and visualisation. 
* /gameboards: csv input with multiple gameboards. 
* /output: contains log.csv, output.csv and visualisation of the startboard and endboard. 
* /docs: contains the design document. 
* /statespace: contains calculations of the state space assignment. 
* main.py: plays the rush hour game and deals with input. 
* PROCESS.md: Contains our working logbook. 

## Authors
* Tjerko Kieft
* Bob Nieuwenhuize
* Kika Banning