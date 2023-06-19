this version introduces threading, global scope, pygame, and the map system


we use threading to run pygame in parrallel with the game and command loop
the pygame loop is a daemon 'background' process that is only able to use variables across the project when they are globalized: thus far only me.location bin classes.py and map_array in locations

map_array format: nxn   n = 9

0 1 2 3 4 5 6 7 8      
1
2
3
4
5
6
7
8




