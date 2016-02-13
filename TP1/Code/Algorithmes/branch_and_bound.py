# Branch-and-Bound Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca


from node import *
from state import *
from math import sqrt

infinity = float('inf')

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def branch_and_bound_search(initialState):
    maxDist = 0
    listPoints = list(initialState.uncoveredPoints)
    for i in range(0, len(listPoints)):
        for j in range(i+1, len(listPoints)):
            maxDist = max(maxDist, dist(listPoints[i],listPoints[j]))
    countMax = 200 + (maxDist/2)**2
    (bound,solution) = bb(Node(initialState),infinity,None, countMax, len(initialState.uncoveredPoints))
    return solution

def bb(node,bound,bestSolution, countMax, nPoints):
    if node.f < bound or len(node.state.antennas) <= nPoints:
        if not node.isRepeated():
            if node.state.isGoal():
                return (node.f,node)
  
            for n in node.expand():
                (newBound,newSolution) = bb(n,bound,bestSolution, countMax, nPoints)
                if newSolution != None:
                    bound = newBound
                    bestSolution = newSolution
                    print bestSolution
            return (bound,bestSolution)
    return (infinity,None)
        
