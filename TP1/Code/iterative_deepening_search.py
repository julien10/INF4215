# Iterative Deepening Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def iterative_deepening_search(initialState):
    for i in range(1000):
        result = rec_df_search(Node(initialState),i)
        if result != None:
            print(i)
            return result


def rec_df_search(node,remainingSteps):
    if remainingSteps > 0:
        if node.state.isGoal():
            node.state.show()
            print 'Steps:', step
            return node
        elif not node.isRepeated():
            for n in  node.expand():
                result = rec_df_search(n,remainingSteps-1)
                if result != None:
                    return result
                
    return None
        
