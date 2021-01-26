# Rush Hour

## Rush Hour 
Rush hour is een puzzel waarbij het doel is om de rode (target) auto naar de uitgang te leiden die recht voor hem ligt. Echter zijn er ook andere voertuigen die de weg versperren, auto’s van twee eenheden lang en trucks van drie eenheden lang. Elk voertuig kan alleen vooruit en achteruit in de richting van zijn positie (horizontaal/verticaal). De opdracht hierbij is dus om de weg naar de uitgang vrij te maken door voertuigen te verplaatsen en de rode (target) auto naar de uitgang te brengen. 

## Description of approach to the algorithms
* Random: hierbij wordt eerst een random voertuig gekozen uit de lijst met alle mogelijke voertuigen die kunnen bewegen. Vervolgens wordt een random move gekozen uit alle mogelijke moves die dat voertuig heeft. 
* Breadth First Search(BFS): voor elke staat van het bord voeren we alle mogelijke beweginge uit die mogelijk zijn om vervolgens de nieuwe staat van het bord toe te voegen aan de queue(FIFO) met alle staten.
    * + archief: Hierbij maken wij ook gebruik van een archief wat bijhoudt welke staat al in het archief staat, als de staat al in het archief staat, werken we hier niet mee verder en dus wordt de staat niet aan de queue toegevoegd.
    * + Beam + heuristieken: We geven aan onze Beam functie de queue mee, deze wordt vervolgens met heuristieken gesorteerd en hiervan worden de 'slechtste' staten afgeknipt. 
        * Beam ratio vs width: eerst hadden wij het idee dat je het best een percentage van de queue lengte kon wegknippen, een beam ratio noemden we dit. Dit brengt alleen risico’s met zich mee, want in Rush Hour is het soms het geval dat je één stap achteruit moet, om er vervolgens twee vooruit te gaan. Het risico hiervan is dus dat je snel de optimale oplossing weg knipt. Hierna vonden we dat 80% van de random puzzels met een 7x7 bord wordt opgelost met een Beam breedte van 10000. Wij gebruiken daarom voor de beam breedte de volgende formule: (bord grootte^2) / (7^2) * 10000.
    * + Priority + heuristieken: Bij onze priority queue doen we in principe hetzelfde als bij de beam search, we geven een queue mee en deze sorteren we. Echter knippen we nu niet de slechtste staten weg, maar deze houden we.
    * + Early solution detection (lookahead): Early solution detection wordt bij ons toegepast op het moment dat we kinderen aanmaken in de BFS, als een kind het bord al oplost, returnen we meteen de oplossing, in plaats van dat het eerst alle andere kinderen nog aanmaakt.
* Iterative Deepening Depth First Search algoritme(IDDFS): dit is eigenlijk een Depth First Search wat voortdurend zijn diepte één stapje omhoog doet totdat een oplossing is gevonden. Dit houdt in dat het algoritme start bij de begin staat, om dan vervolgens alle mogelijke staten tot een bepaalde diepte te doorzoeken. Het nadeel van de IDDFS is dat het erg veel tijd kost om tot een oplossing te komen, dus waar bij BFS het probleem het geheugen is, is dit bij IDDFS de tijd. Dit wordt veroorzaakt doordat de hele zoekboom weer opnieuw doorlopen moet worden met Depth First Search bij het verhogen van de diepte met één. Dat betekent veel dubbel onnodig werk.
    * + Heuristieken: Om het proces van de IDDFS te versnellen hebben wij gebruik gemaakt van een heuristiek die het minimaal aantal verplichte moves berekent en vanaf die diepte pas gaat zoeken. 

## Requirements
Deze codebase is volledig geschreven in Python 3.8.5 t/m 3.9.1. 
Onderstaande packages om deze code te draaien staan in requirements.txt en zijn te installeren met behulp van pip: "pip install -r requirements.txt"
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