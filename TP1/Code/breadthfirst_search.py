# Breadth-first Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def breadthfirst_search(initialState):
    step=0
    frontier = [Node(initialState)]
    visited = set()
    while frontier:
        node = frontier.pop(0)
        visited.add(node.state)
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
            frontier = frontier + [child for child in node.expand() if child.state not in visited]
    return None
