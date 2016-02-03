# A* Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *
from math import sqrt

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def astar_search(initialState):
    step = 0
    maxDist = 0
    listPoints = list(initialState.uncoveredPoints)
    for i in range(0, len(listPoints)):
        for j in range(i+1, len(listPoints)):
            maxDist = max(maxDist, dist(listPoints[i],listPoints[j]))

    frontier = [Node(initialState)]
    cout = 0
    while frontier and cout <= 200 + (maxDist/2)**2:
        node = frontier.pop(0)
        step += 1
        # if len(node.state.antennas):
        # Modifier le code car il additionne tous les couts de toutes les branches
        cout += node.g
        if step % 1000 == 0:
            print step
        # node.state.show()
        # print '----------------'
        if node.state.isGoal():
            node.state.show()
            print 'Cost:', node.g
            print 'Steps:', step
            return node
        elif node.isRepeated():
            continue
        else:
            frontier = frontier + node.expand()
            frontier.sort(cmp = lambda n1,n2: -1 if n1.f < n2.f else (1 if n1.f > n2.f else 0))
    return None
