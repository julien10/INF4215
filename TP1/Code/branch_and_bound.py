# Branch-and-Bound Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca


from node import *
from state import *

infinity = float('inf')

def branch_and_bound_search(initialState):
    (bound,solution) = bb(Node(initialState),infinity,None)
    return solution

def bb(node,bound,bestSolution):
    if node.f < bound:
        if not node.isRepeated():
            if node.state.isGoal():
                return (node.f,node)
  
            for n in node.expand():
                (newBound,newSolution) = bb(n,bound,bestSolution)
                if newSolution != None:
                    bound = newBound
                    bestSolution = newSolution
            return (bound,bestSolution)
    return (infinity,None)
        
