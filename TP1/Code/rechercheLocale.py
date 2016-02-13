__author__ = 'Julien Antoine et Abdlhadi Temmar'


import time
from math import *
from copy import deepcopy

from Algorithmes.localSearchMadeHome import *

from Algorithmes.node import *

from Algorithmes.simulated_annealing import *

grille = (50,50)
# grille = (30, 30)
K = 200
C = 1
initialUncoveredPoints = 0
points30 = [(10, 2),(8, 9),(23, 9),(14, 10), (29, 10), (17, 14), (4, 23), (28, 23), (29, 25), (17, 29)]
# points30 = [(10, 2),(8, 9), (29, 10), (4, 23), (29, 25), (17, 29)]    # points ecartes
# points30 = [(10, 2),(8, 9), (29, 10), (23, 9), (14, 10), (17, 14)]      # points en haut
points15 = [(10,3),(4,9),(8,10),(13,9),(14,11),(2,15)]
points50 = [(10, 10),(20,20),(30, 0),(30, 40),(50, 40)]
points5 = [(1, 1),(2,2),(3, 0),(3, 4),(5, 4)]


def search(points, k, c):
    solution = localSearch(RechercheLocale(points), k, c)
    return [(x,y,r) for (x,y,r,list) in solution]



class RechercheLocale(State):
    def __init__(self,points):
        self.uncoveredPoints = set(points)
        # self.antennas = set([(x, y, sqrt(2)) for x in range(1, grille[0], 2) for y in range(1, grille[0], 2)])
        self.antennas = [(x, y, 1, [(x, y)]) for (x,y) in points]
        self.initialUncoveredPoints = len(points)
        self.cout = 0


print '**************************************************************************'
print 'Julien et Abdelhadi sont fiers de vous presenter leur nouvel algorithme :3'
print '**************************************************************************'
start = time.time()
solution = search(points50, K, C)
end = time.time()
print str(solution)
print '*******************************'
print '* En seulement {} seconds :D *'.format(end-start)
print '*******************************'


