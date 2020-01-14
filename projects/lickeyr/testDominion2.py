# -*- coding: utf-8 -*-
"""
Created on Mon January 13th, 2020
@author: lickeyr
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV = testUtility.numVic(player_names)
nC = -10 + 10 * len(player_names)

#define box
box = testUtility.GetBoxes(nV)

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
supply = testUtility.getSupply(box)

#The supply always has these cards
testUtility.setSupply(player_names, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayers()

#Play the game
testUtility.playGame(supply, supply_order, players, trash)

#Final score
testUtility.score(players)