# Algorithms
* BFS.py: the Breath-first algorithm, seeking all possible states. 
    * With archive and early solution detection (lookahead)
* IDDFS.py: the Iterative Deepening Depth-First search, seeking all possible states. 
    * With heuristic 9 (start checking from depth of minimum number of required moves)
* biggest_step.py: the BFS in combination with the heuristic that first the biggest step for all vehicles is performed and then the other steps in order of the size of the steps. 
* play_yourself.py: which gives the ability to play the game yourself, asking for inputs. 
* Priority.py: contains Priority queue search and option for Beam search, using multiple heuristicks. 
* randomise.py: the Random algorithm picking a random vehicle from the possible moves and then picking a random move from the possible moves for that vehicle. 
    * Set sample size to run this algorithm multiple times. 

# Heuristics used for Priority queue search and Beam search:
* H1: maximal number of free spaces ahead of the target car
* H2: minimum number of vehicles blocking the target car
* H3: minimum distance to the goal position for the target car
* H4: H2 + H3 
* H5: H2 + H3 + H8
* H6: H2 + H8
* H7: most possible moves per state 
* H8: minimum number of blocked blocking vehicles
* H9: minimum number of required moves