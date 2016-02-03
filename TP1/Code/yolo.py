__author__ = 'juanta tout seul'
# video.py
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca
# Date:   Januay 7th 2015
#
# This problem consists in selecting a set of videoa that cover a list of topics
# given as input, such that their total duration is minimized

import sys
sys.path.append('../Algorithmes')

from node import *
from state import *
from breadthfirst_search import *
from depthfirst_search import *
from lowestcost_search import *
from iterative_deepening_search import *
from astar_search import *
from math import sqrt
from copy import deepcopy

grille = (15,15)
K = 200
C = 1

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)


class AntennaState(State):
    def __init__(self,points):
        self.uncoveredPoints = set(points)
        self.antennas = set()

    # def equals(self,otherState):
    #     return ( self.chosenVideos == otherState.chosenVideos and
    #              self.uncoveredTopics == otherState.uncoveredTopics)

    def show(self):
        print( self.antennas, self.uncoveredPoints )

    def executeAction(self,action):
        (actionName, (x,y,r)) = action
        if actionName == 'add':
            self.antennas.add((x,y,r))
            listPoints = deepcopy(self.uncoveredPoints)
            for p in listPoints:
                if dist(p,(x,y)) <= r:
                    self.uncoveredPoints.remove(p)

    def possibleActions(self):
        x = range(0,grille[0])
        y = range(0,grille[1])
        coordonnees = []
        for xx in x:
            for yy in y:
                for r in range(1,grille[0]/2 + 1):
                    for (xPoint,yPoint) in self.uncoveredPoints:
                        if dist((xx,yy),(xPoint,yPoint)) - r < 0.5:
                            coordonnees.append(('add',(xx,yy,r)))
                            break
        return coordonnees

    def cost(self,action):
        (actionName, (x,y,r)) = action
        return K + C*r**2

    def isGoal(self):
        return len(self.uncoveredPoints) == 0

    def heuristic(self):
        rayons = 0
        for (x,y,r) in self.antennas:
            rayons += C*r**2
        return len(self.antennas)*200 + rayons


solution = astar_search(AntennaState([(10,3),(4,9),(8,10),(13,9),(14,11),(2,15)]))

