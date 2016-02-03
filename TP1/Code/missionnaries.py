# video.py
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca
# Date:   Januay 7th 2015
#
# Representation of the problem of missionaries and cannibals

import sys
sys.path.append('../Algorithmes')

from node import *
from state import *
from breadthfirst_search import *
from depthfirst_search import *
from lowestcost_search import *


def invert(side):
    if side == 'left':
        return 'right'
    else:
        return 'left'

class RiverState(State):
    def __init__(self):
        self.people = { 'left': {'cannibal': 3, 'missionary': 3 },
                        'right': { 'cannibal': 0, 'missionary': 0 } }
        self.boatLocation = 'left'
        
    def equals(self,otherState):
        return (self.people == otherState.people and
                self.boatLocation == otherState.boatLocation)

    def show(self):
        print(self.people, self.boatLocation)

    def executeAction(self,inBoat):
        for p in inBoat:
            self.people[self.boatLocation][p] -= 1
            self.people[invert(self.boatLocation)][p] += 1
        self.boatLocation = invert(self.boatLocation)
        
    def possibleActions(self):
        possibleActions = []

        # If moving one or two missionaries, we need to check if it will OK on both sides
        if self.people[self.boatLocation]['missionary'] > 0:
            if (self.__check({'missionary': self.people[self.boatLocation]['missionary'] - 1,
                             'cannibal': self.people[self.boatLocation]['cannibal']}) and
                self.__check({'missionary': self.people[invert(self.boatLocation)]['missionary'] + 1,
                             'cannibal': self.people[invert(self.boatLocation)]['cannibal']})):
                possibleActions.append(['missionary'])
        if self.people[self.boatLocation]['missionary'] > 1:
            if (self.__check({'missionary': self.people[self.boatLocation]['missionary'] - 2,
                             'cannibal': self.people[self.boatLocation]['cannibal']}) and 
                self.__check({'missionary': self.people[invert(self.boatLocation)]['missionary'] + 2,
                             'cannibal': self.people[invert(self.boatLocation)]['cannibal']})):
                possibleActions.append(['missionary','missionary'])

        # For cannibal, we only need to check if it will be OK on the other side
        if self.people[self.boatLocation]['cannibal'] > 0:
            if self.__check({'cannibal': self.people[invert(self.boatLocation)]['cannibal'] + 1,
                             'missionary': self.people[invert(self.boatLocation)]['missionary']}):
                possibleActions.append(['cannibal'])
        if self.people[self.boatLocation]['cannibal'] > 1:
            if self.__check({'cannibal': self.people[invert(self.boatLocation)]['cannibal'] + 2,
                             'missionary': self.people[invert(self.boatLocation)]['missionary']}):
                possibleActions.append(['cannibal','cannibal'])
                   
        # If moving a cannibal and a missionary,  we only need to check if it will be OK on the other side       
        if self.people[self.boatLocation]['missionary'] > 0 and self.people[self.boatLocation]['missionary'] > 0:
            if self.__check({'cannibal': self.people[invert(self.boatLocation)]['cannibal'] + 1,
                             'missionary': self.people[invert(self.boatLocation)]['missionary'] + 1}):
                possibleActions.append(['cannibal','missionary'])
 
        return possibleActions
    
    def cost(self,action):
        return 1

    def isGoal(self):
        return self.people['left']['cannibal'] == 0 and self.people['left']['missionary'] == 0
    

    def __check(self,group):
        return (group['cannibal'] == 0 or group['missionary'] == 0 or group['cannibal']  <= group['missionary'])
        
solution = lowestcost_search(RiverState())

print solution.extractSolution()
