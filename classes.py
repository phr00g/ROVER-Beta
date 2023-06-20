#classes for player, and locations (locations should be nodes with 4 edges: north, south, east and west)
import os

class person:
    def __init__(self):
        self.name = None
        self.inventory = {} #item.name:item
        self.location = ''
        self.minerals = 0
        self.wincondition = False
        self.energy = 3
        

    



class location:
    def __init__(self,x,y):
        self.x = None
        self.y = None
        self.name = None  
        self.greeting = ''  #here we put the greeting along the lines of, you see a bank with a green window, to the west there is fog, and you are surrounded by a great brick wall from the north, east, and south
        self.inventory = {} #dict for all items that the player can PICK UP and add to their inventory item.name:item
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        #explanations for inabliltiy to travel in direction: whynot['north'] = the door is locked
        self.whynot = {}
        self.persons = {} #says who is in location     person.name:person
        self.istestable = False
        self.hasbeentested = False
        self.desc = "" #description of locaiton in greeting of adjacent and connected locaitons
        self.hasmineral = False
        self.hasevent = False
        self.firsttime = True
        self.eventflag = False
        #turns true when player tests location, and it is suitable for excavation
        self.success = False
    def update(self):
        pass

    def event(self):
        pass


        

        # we need descriptinos for what is north south etc , especially for when we cant go in those directions

class item:
    def __init__(self,name): #to destroy the objects, trash array/dict????
        self.name = name
        
        
        self.isgone = None
        
        self.interactables = {} #dict of items with which current item can interact with itemname:itemvar
        self.verbs = {}
        self.prepositions = []  #prepositions that are valid in command before item
        self.onpickup = "You picked up a {}".format(self.name) #append to string if you want more to happen
        self.ondrop = "You dropped the {}".format(self.name) #append to string if you want more to happen
        self.onpickupgreeting = None #message to add to location greeting after item gets pickedup
        self.directobjects = {} #
        self.iscrystal = False
        self.isalive = False
        self.isrelic = False
        self.greeting = ""




class NPC(person):
    def __init__(self,name):
        super().__init__()
        self.name = name
        
        self.verbs = {}
        self.deathscream = ''''''
        self.greeting = ""
        self.giftable = True
        #must add to distinguish between person and item
        self.isalive = True

    def ongift(self):
        pass
        


        




#instantiations, we must creater player controller object here
gamegoing = True
global me
me = person()


