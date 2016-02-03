# Lowest-cost Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *
from math import sqrt
from math import ceil

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def maxDist(self):
        maxDist = 0
        listPoints = list(self.uncoveredPoints)
        for i in range(0, len(listPoints)):
            for j in range(i+1, len(listPoints)):
                maxDist = max(maxDist, dist(listPoints[i],listPoints[j]))
        return maxDist

def lowestcost_search(initialState):
    step = 0
    frontier = [Node(initialState)]
    visited = set()
    coutMax = 200 + (ceil(maxDist(initialState)/2))**2
    while frontier:
        node = frontier.pop(0)
        visited.add(node.state)
        step += 1
        # node.state.show()
        # print '----------------'
        if node.state.isGoal():
            node.state.show()
            print 'Cost:', node.g
            print 'Steps:', step
            return node
        else:
            frontier = frontier + [child for child in node.expand() if child.state not in visited]
            frontier.sort(cmp = lambda n1,n2: -1 if n1.g < n2.g else (1 if n1.g > n2.g else 0))
    return None
