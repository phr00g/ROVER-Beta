
from classes import *
from locations import *
from items import *
from tokenhandler import *
import random
import pygame
import time
import threading
from pgmap import *
from methods import *
from NPCs import *
import sys


       
 

# #game start555%55%

#intro sequence
print('\n')
idnumber = str(random.randint(1000,9999))
print_wrapped_text('\n')
print_wrapped_text("Greetings on behalf of Material Solutions Incorporated (MSI), Associate Remote ROVER Engineer #{}!  ".format(idnumber))
print_wrapped_text("It seems that this is your first time uplinking to a ROVER! ")
print_wrapped_text('\n')
print_wrapped_text("As you know, Associated Remote ROVER Engineer #{}, MSI's TS909 ROVER is a simple little soil testing and drilling rig. We wish you could see how cute it is!".format(idnumber))
print_wrapped_text("MSI is looking for available and ethically reachable deposits of Neutronium , which is why your ROVER is currently located on the conveniently nearby terrestrial planet of REDACTED.\n")
print_wrapped_text("Excitingly you are part of the first probe that we have sent to this planet! Our satellite scan shows that there is no significant intelligent life on this planet. In the extremely unlikelty event that you do encounter some low level lifeform, please do not acknowledge it and carry on with your mission. ")

print_wrapped_text("You you already well know your ROVER is an extremely simple device. You can issue it two types of commands: one token and two token\n")
print_wrapped_text("For example, if you type in 'inventory' your ROVER will list all the items in your inventory. This is a one token command. \n")
print_wrapped_text("Two token commands are two words, for example typing in 'go west' will make your ROVER go to the west. As far as movement goes, you can move in the north, south, east and west directions.")
print_wrapped_text("Type in 'test soil' to test your location and determine if it is a suitable excavation site.  Type in 'drill' followed by an object to drill into it, such as 'drill tree'. ")
print_wrapped_text("Both using 'test soil' and 'drill' both will cost you one point of energy. You start with 3 energy, and you can get more by using: 'pickup crystal' to gather energy crystal.")
print_wrapped_text("Lastly you can check your energy level by typing in 'energy', you can see how many suitable excavation sites you have found by typing in 'progress', and you can see what is in your inventory by typing in 'inventory'. ")
print_wrapped_text("\nType in 'help' to be listed all of the possible commands if you ever forget.")
print_wrapped_text("This is the full extent of your ROVER's capabilites. Typing in nonexistent or unauthorized commands will risk breaking your ROVER and a possible infraction.")
print_wrapped_text("Please locate and test (six) suitable excavation sites, and return your ROVER safely back to its landing dock. When you leave, you will see that the landing dock is marked orange on your map grid. ")
print_wrapped_text("Good luck, and we know you will be successful!\n\n")
print('\n')


#game loop, DECLARE PLAYER STARTING LOCATION BEFORE ENTERING GAMELOOP
#                  [column][row]
me.location = map_array[3][4] 






running = True




while gamegoing:

    #consider refresh method / game tick: here location change tick

    
    #for when player returns to landingdock: a3, and has win condition -----> end game
    if me.location == landing and me.wincondition == True:
        print_wrapped_text("Congratualtions Associated Remote ROVER Engineer #{}, your missions was a success! You will now be disconnected from your ROVER. Please sign back on tomorrow at 7:00 am for your next assignment. ".format(idnumber))
        quit()

#####################################TEST CONDITION AREA REMEMBER TO REMOVE AFTER USE##############################
    


###################################################################################################################




    #must update every time which is stupid
    loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}


    #CHANGE THIS, IF ME.LOCAITON.EVENTFLAG == TRUE THEN ME.LOCATION.EVENT
    if me.location.eventflag == True:
        
        me.location.event()

    
    

    #show greeting for specific location that just entered
    
    #if there are items in location, print_wrapped_text their greeting so we dont forget their existence -- add this to look 
    look()
    
    #now that we have visitied with location, its firstime attribtue is false and must stay that way
    me.location.firsttime = False

    #at the moment arbitrary condition for command loop
    commanding  = True

    #begin command loop
    while commanding:
        loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}
        
        #consider refresh / command tick method
        
        command = input("\nEXECUTE COMMAND:").lower()
        print_wrapped_text('\n')
        command = command.split()
        if len(command) == 0:
            continue
        verb = command[0]

        if verb == 'quit':
            quit()


        #handles location changing and failure to do so   special case for walking 
        if verb == 'go' or verb == 'walk':

            #if they only say go or walk
            if len(command) == 1:
                print_wrapped_text("Where do you want to {} ?".format(verb))
                continue

            # me.location.west == None
            if command[1] not in loc_dict  or loc_dict[command[1]] == None :
                print_wrapped_text("You can not go {} \n".format(command[1]))
                
                if command[1] in me.location.whynot:
                    print_wrapped_text(me.location.whynot[command[1]])

                continue

            #player goes in new direciton --> update player locaiton --> end command loop
            else:
                
                #we can probably make this a controller class method
                nextLocation = loc_dict[command[1]]
                me.location =  nextLocation
                
                break


        #checks to see if there is a valid verb in command
        if verb in verbs:
            
            pass
        else:
            print_wrapped_text("ROVER:I can only understand commands that start with a verb.")
            continue
        

        
        
        #finds number of tokens in command and sends command array to appropraite handler method    
        tokenhandler(command)
        

        

        #print_wrapped_text empty line5
        print_wrapped_text("\n")






    






