# Recursive Depth-first Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *

def recursive_depthfirst_search(initialState):
    return rec_df_search(Node(initialState))

def rec_df_search(node):
    if node.state.isGoal():
        node.state.show()
        return node
    elif not node.isRepeated():
        for n in node.expand():
            result = rec_df_search(n)
            if result:
                return result
        return None
        
