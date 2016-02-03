# Depth-first Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def depthfirst_search(initialState):
    step=0
    frontier = [Node(initialState)]
    while frontier:
        node = frontier.pop(0)
        step+=1
        # node.state.show()
        # print '----------------'
        if node.state.isGoal():
            node.state.show()
            print 'Steps:', step
            return node
        elif node.isRepeated():
            continue
        else:
            frontier = node.expand() + frontier
    return None
