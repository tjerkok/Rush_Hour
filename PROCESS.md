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

### Bob
Made the initial classes, an option to play the game yourself as well as a random algorithm which solves the game. Also made the requested output.

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

### Bob
We worked together this day, so I worked on the same things as Tjerko and Kika.

## 13 january 2021

### Kika
We ran all boards with the BFS and all boards 1000x with the Random algorithm, so we would have results to compare voor the Baseline Deadline of today. We discussed the results and formulated them in the Baseline PDF. 

### Tjerko
Worked on the baseline together with Kika and Bob.

### Bob
Also worked on the baseline which we had to submit today.

## 14 january 2021
### Tjerko
Trying to implement beam search on the Breadth First Search.

### Kika
Discussed options for improvement of the breadth First and came to the idea of the beam search. With the heuristic that we only pick a move from the moves with the greatest amount of free spaces ahead of the target car. 

### Bob
We worked together again so I did the same things as Tjerko and Kika. We also discussed the baseline and potential improvements with Kiara and Quinten.

## 15 january 2021
### Tjerko
We worked on improving the Breadth First Search algorithm. I figured out how to let the BFS only use deepcopy when there'll be a new state after moving. If the move created a state that's in the archive, deepcopy will be avoided. 

### Kika
Added the priority search and tried serializing, however did this not give us any improvements. 

### Bob
At the beginning of the day we worked together trying to improve the Breadth First Search algorithm. Then we split up and I was responsible to get out output through the check50 check, so I did that.

## 18 january 2021
### Kika
We worked on the deadline 'First Algorithm', I focused on writing the text.

### Bob
Also worked on the first algorithm pdf.

### Tjerko
Even I was working on the First Algorithm pdf.

## 19 january 2021
### Tjerko
Set algorithms in classes

### Kika
We discussed what our next steps would be, we chose for implementing Iterative deepening depth search and implemented that. Also we adjusted our algorithm by making classes of them with multiple functions. 

### Bob
Worked together on our algorithms.

## 20 january 2021
### Tjerko
- iddfs
- meeting
- Trying to find best way to archive states on depth1, while other later found states on depth2, similar to archived state, are not skipped when depth1 > depth2.
    * IDDFS (testboard6x6):
        * Archiving with dictionary, key = hash, value = depth. states: 3531. moves: 8.
        * Archiving with original set (losing most efficient solution, might not even find one). states: 741. moves: 10.
Concluded the best way for the IDDFS to archive was a dictionary. Even while it was slow, it does give a solution for the problem, whereas an archive set didn't depend on the depth of the found state, which is way less efficient.

### Kika
We fixed the Iterative deepening depth search, we discussed our next steps and we had a meeting with Kiara and Quinten. 
I focused on researching the magic number of apply_priority for the priority search. Also I did some research on a possible extension for breadth first search. 

### Bob
Tried to find out what beam width/beam ratio would be good to use and ran some tests to find out as well as searched on internet if there were any papers about it.

## 21 january 2021
### Kika
Worked on the practice presentation, did some research after the differences between the heuristics. 
Tried working out a new idea where the biggest possible steps are taken first. 
Improved heuristics code for priority and beam. 

### Bob
Added a Heuristic which calculates the minimum moves required and uses that for our beam search/ priority queue and IDDFS

### Tjerko
Worked on the practice presentation and getting the results for the presentation.

## 22 january 2021
### Bob
We had the practice presentation today and after that I fixed some things about the heuristic I added yesterday, because it wasn't correct yet.

### Kika 
We did the last preparations for the practice presentation and we listened and presented during the practice presentations. 

### Tjerko
Did the practice presentation.

## 25 january 2021 
### Kika
We worked on Algorithm 2, we discussed our next stepps, we divided our To Do list and worked on that.

## Tjerko
Worked on the Second Algorithm pdf and started cleaning up the repository (adding comments, fixing duplicate code etc).

### Bob
Worked on the second algorithm pdf as well and tried to fix the duplicate code in our board class a little bit.

## 26 january 2021 
### Kika


## Tjerko


### Bob
Fix the duplicate code in our board class
