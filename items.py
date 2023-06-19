from methods import *
from classes import *
#to stop random complaints
from methods import pickup,drop,verbs



torch = item('torch')
torch.verbs['pickup'] = pickup
torch.verbs['drop'] = drop

#at landing
crystal1 = item('crystal')
crystal1.verbs['pickup'] = pickup
crystal1.iscrystal = True
crystal1.greeting = "There appears to be an energy crystal on the floor."


#on dead roger body
crystal2 = item('crystal')
crystal2.verbs['pickup'] = pickup
crystal2.iscrystal = True


#tree and relic in mouth of cellulose forest
tree = item('tree')
tree.verbs['drill'] = drill
tree.greeting = 'There is a noteworthy tree here within reach, it is by far the tallest one in view.'




star = item('star')
star.verbs['pickup'] = pickup
star.verbs['give'] = give
star.verbs['drop'] = drop
star.isrelic = True
star.greeting = 'There appears to be a star shaped trinket on the floor'

#DEAD ROVER IN FOREST EAST HAS LIGHT AND ONE CRYSTAL

flashlight = item('flashlight')
flashlight.verbs['pickup'] = pickup
flashlight.onpickupgreeting = 'We can use this to see in the dark!'


#lever in level 2 of cave

lever = item('lever')
lever.verbs['pull'] = pull
lever.verbs['use'] = pull
lever.greeting = '''There is some sort of lever fixed agains the cave wall.'''
###