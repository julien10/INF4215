# Depth-first Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *
from math import sqrt,ceil

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def depthfirst_search(initialState):
    step=0
    frontier = [Node(initialState)]

    (minX, minY) = map(min, zip(*initialState.uncoveredPoints))
    (maxX, maxY) = map(max, zip(*initialState.uncoveredPoints))

    maxDist = dist((minX, minY), (maxX, maxY)) / 2
    coutMax = 200 + (ceil(maxDist))**2
    print coutMax
    while frontier:
        node = frontier.pop(0)
        step+=1
        # print '----------------'
        if node.isRepeated():
            #print "cout : " + str(node.g)
            continue
        elif node.state.isGoal():
            node.state.show()
            print 'Cost:', node.g
            print 'Steps:', step
            return node
        else:
            frontier = node.expand() + frontier
    return None
