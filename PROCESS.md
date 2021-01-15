# Process

## 4 january 2021 - 11 january 2021

### Tjerko
We discussed how we'll approach and structure the representation. I did the visualization and decided to use a Matplotlib heatmap. The heatmap gives the possibility to visualize the numpy array and easily add colors to the places in the array. 

### Kika
* Calculated state space
* Made the UML diagram (/docs/design.uxf)
* Added README
* Added comments and docstrings
* Together we discussed the datastructure and programmed the main

## 11 january 2021
Meeting with Kiara and Quinten.
Added issues:
- Update Process.md
- Find best way to hash/serialize np.array/states
- Add git ignore
- Keep track of state space for solutions (amount of states)
- Deadline Baseline

## 12 january 2021
### Tjerko
We worked together on finding out how to use the Breadth First algorithm. We decided to let the script add to a log.csv all the details of every time we finished a game board. As usage, we added a algorithm cmd argument, so we can specify the algorithm to use when you run the script. The Breadth First method works, with memory, so it won't add a child to the queue when it's a state that's already known. We still need to figure out a way to make the algorithm faster, by hashing/serializing objects better. Right now we have a set of hashed, converted to string numpy arrays, to check if a state is already known. This still takes up some space, but we need to figure out how much more space it takes than a numpy array.

### Kika
Decided to use the Hash function for checking if a state was already used. However for further use we might want to use this function more, as we can not solve the 12x12 board yet, due to memory issues. 
We decided to keep track of all our solutions in log.csv so we could do a little research and to compare multiple algorithms. We added the testboard for fast checking and we made the BFS algorithm work.

## 13 january 2021

### Kika
We ran all boards with the BFS and all boards 1000x with the Random algorithm, so we would have results to compare voor the Baseline Deadline of today. We discussed the results and formulated them in the Baseline PDF. 

### Tjerko
Worked on the baseline together with Kika and Bob.

## 14 january 2021
### Tjerko
Trying to implement beam search on the Breadth First Search.

### Kika
Discussed options for improvement of the breadth First and came to the idea of the beam search. With the heuristic that we only pick a move from the moves with the greatest amount of free spaces ahead of the target car. 