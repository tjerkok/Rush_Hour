# State Space
## Tjerko

### Opdracht 1
n = 20

r = 12

aantal verschillende roosters = 20!/(20-12)! = 6.03398316×10^13

### Opdracht 2
n = 3

r = 20

verschillende routes = 3^20 = 3.4867844×10^9

### Opdracht 3
n = 3

r = 25

verschillende ladingen = 3^25 = 8.47288609×10^11

### Opdracht 4
n = 110

r = 30

verschillende manieren = 110!/(30!(110-30)!) = 8.36623092×10^26

r = 31

verschillende manieren = 110!/(31!(110-31)!) = 2.15902733×10^27

r= 32 

verschillende manieren = 110!/(32!(110-32)!) = 5.33009873×10^27

### Opdracht 5
n = 26

r = 7

mogelijkheden = 26!/(26-7)! = 4.90584303×10^43

kans van winnen = 1/mogelijkheden = 1.95434865×10^−4

### Opdracht 6
eerst 30 dozen:

r = 30

n = 3

verschillende ladingen = 3^30 = 2.05891132×10^14


dan 15 dozen met 2 mogelijkheden:

r = 15

n = 2

verschillende ladingen = 2^15 = 32768


totale mogelijkheden= 3^30 * 2^15 = 6.74664062×10^18

### Opdracht 7

#### Variabelen:
- Breedte speelveld
- Auto's
- Vrachtwagens

#### Versimpelende aannames:
- Alle auto's en vrachtwagens kunnen vooruit en achteruit
- De auto's en vrachtwagens kunnen over elkaar heen bewegen

Hierdoor zal de werkelijke state space grootte nooit hierboven komen, omdat in het echte spel het aantal mogelijkheden voor de auto's en vrachtwagens lager is omdat ze niet over elkaar heen kunnen bewegen.

#### Formule bovengrens state space

Het aantal auto's is *r* en het aantal mogelijkheden om te bewegen is *n*. Het aantal mogelijkheden om te bewegen ligt aan de breedte van het spelbord *l*, hierdoor is *n = l - 1* voor auto's.

Het aantal vrachtwagens is *s* en het aantal mogelijkheden om te bewegen is *m = l - 2* vanwege de lengte van de vrachtwagen.

De state space voor auto's is *R = (l - 1)^r*. Voor vrachtwagens *T = (l - 2)^s*. De totale state space is *S = R * T*.

#### Klein voorbeeld

Op een bord van 4x4 met twee auto's, allebei horizontaal, geplaatst op de eerste en tweede rij.

Alle mogelijkheden zijn:
```
--..
--..
....
....

--..
.--.
....
....

--..
..--
....
....

.--.
--..
....
....

.--.
.--.
....
....

.--.
..--
....
....

..--
--..
....
....

..--
.--.
....
....

..--
..--
....
....

```

Dus negen mogelijkheden. In de formule voor de totale state space *S* met *l* = 4, *r* = 2 en *s* = 0 is *S = (4 - 1)^2 * (4 - 2)^0 = 9*. Hier klopt de formule dus.

#### Game #1

Game #1 heeft twaalf auto's en één vrachtwagen. Het speelbord is zes bij zes. Dus *l* = 6, *r* = 12 en *s* = 1. De totale state space is *S = (6 - 1)^12 * (6 - 2)^1 = 976562500*. De werkelijke state space grootte zal hier dus ver onder liggen, omdat het bord te vol is om werkelijk zoveel mogelijkheden te hebben, vanwege de aanname dat auto's en vrachtwagens over elkaar kunnen bewegen.