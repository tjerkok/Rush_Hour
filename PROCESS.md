# Process

## 4 january 2021 - 11 january 2021

### Tjerko
We discussed how we'll approach and structure the representation. I did the visualization and decided to use a Matplotlib heatmap. The heatmap gives the possibility to visualize the numpy array and easily add colors to the places in the array. 

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