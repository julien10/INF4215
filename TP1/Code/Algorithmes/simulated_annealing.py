# Hill-climbing Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *
import random
from math import exp


def decrease(t):
    return t*0.9

def simulated_annealing_search(initialState,T = 100,limit = 0.1,maxSteps = 1000):
    temperature = T
    node = Node(initialState)
    while temperature > limit:
        print temperature
        step = maxSteps
        while step > 0:
            if node.state.isGoal():
                node.state.show()
                return node
            else:
                candidate = random.choice(node.expand())
                if candidate.h < node.h:
                    node = candidate
                elif random.random() < exp(float(node.h - candidate.h)/temperature):
                    node = candidate
                step -= 1
        temperature = decrease(temperature)
    return None
