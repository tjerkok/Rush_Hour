# State Space 
## Kika

N = Different types / choices each time

R = Times 

Types: 
* Combination with repetition
* Combination without repetition
* Permutation with repetition
* Permutation without repetition

### Opdracht 1 studievakken
Permutation without repetition

N = 20 
R = 12 

Verschillende roosters: 6.03 * 10^13

### Opdracht 2 fietsroutes

Permutation with repetition

N = 3
R = 20 

Verschillende routes: 34.9 * 10^8

### Opdracht 3 Dozen 
Combination with repetition

N = 3
R = 25

Verschillende ladingen: 351 

### Opdracht 4 Vakken 
Combination without repetition

N = 110
R = 30
Combinaties van vakken: 83.7 × 10^25

R = 31
Combinaties van vakken: 21.6 × 10^26

R = 32: 
Combinaties van vakken: 53.3 × 10^26

### Opdracht 5 Loterij
Permutation without repetition 

N = 26
R = 7

Aantal mogelijke trekkingen: 33.1 * 10^8
Kans op winnen: 3.0 * 10^-10

### Opdracht 6 Dozen 2.0
Combination with repetition

N = 45
R = 3 
Dit opsplitsen...

N = 30
R = 3 
verschillende ladingen 1: 496

N = 15
R = 2
Verschillende ladingen 2: 16
Optelling 1 + 2: 512

### Opdracht 7
Permutation with repetition
1. Welke case heb je gekozen: Rush Hour
2. Welke variabelen zijn er in de case: 
    * R: Hoeveelheid auto's 
    * N: De mogelijke stappen die een auto maakt: Lengte grid - 1 (voor auto's), lengte grid - 2 (voor trucs)
    * Aantal keer dat je een 'move' maakt 
    * Verschillende groottes van borden 
3. Beschrijf de eventuele versimpelende aannames die je maakt en waarom de werkelijke state-space grootte hier dan gegarandeerd nooit boven ligt.
    * Je doet de aanname dat iedere auto op elke ‘stap’ kan staan, maar dit kan niet altijd omdat er dan mogelijk andere auto’s in de weg staan. Dit zorgt wel dat je echt het maximum aantal auto’s verkrijgt. 
4. Geef de formule voor de berekening van (de bovengrens van) de grootte van de state-space van je case.
    * N^r
    * Een auto mag namelijk bij verschillende states op dezelfde plek staan, zo kan er toch een ander bord ontstaan als een andere auto wel is verschoven. 
    * Verschillende volgordes van auto's maken uit, iedere auto is anders. 
5. Laat in een klein voorbeeld zien dat de formule klopt door bijvoorbeeld alle staten op te sommen.
    * Voor een 3x3 grid met 2 horizontale auto's: 
    xx-     xx-     -xx     -xx
    xx-     -xx     xx-     -xx
    ---     ---     ---     ---
    Hierbij is N: 3-1
    R: 2 auto's 
    2^2 = 4 opties state spaces. 
6. Bereken de grootte van de state-space voor één of meer van de probleem-instanties in de case.
    * Grid: 6x6_1
    * Rauto = Aantal auto's: 12
    * Rtruc = 1
    * Nauto = 6 - 1 = 5
    * Ntruc = 6 - 2 = 4
    * 5^12 * 4^1 = 97.6 * 10^7

