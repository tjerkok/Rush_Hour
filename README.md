# Rush Hour
Rush Hour seems to be an easy puzzle, altough it has a surprising challenging character. In a square field with varying dimensions is a black car named 'X', your car. This cars must go to the exit, which is placed right in front of the car. However, other vehicles, cars of two units and trucs of three units, that may only be moved in their direction of travel, block the way to the exit. The vehicles are not aloud to turn around. The assignment is simple: clear the way to the exit by moving other vehicles and move your black car to the exit. 

## Requirements

## Usage
python3 main.py [gameboards/"gamename".csv]

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
* Bob Nieuwehuizen
* Kika Banning 