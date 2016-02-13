__author__ = 'Julien Antoine et Abdlhadi Temmar'


import time
from math import *
from copy import deepcopy
import Tkinter as tk
from random import *

from Algorithmes.localSearchMadeHome import *

from Algorithmes.node import *

from Algorithmes.simulated_annealing import *

grille = (50,50)
# grille = (30, 30)
K = 200
C = 1
# points30 = [(10, 2),(8, 9),(23, 9),(14, 10), (29, 10), (17, 14), (4, 23), (28, 23), (29, 25), (17, 29)]
# points30 = [(10, 2),(8, 9), (29, 10), (4, 23), (29, 25), (17, 29)]    # points ecartes
# points30 = [(10, 2),(8, 9), (29, 10), (23, 9), (14, 10), (17, 14)]      # points en haut
points30 = [(x,y) for x in range(5,11) for y in range(5,11)]
points30.extend([(x,y) for x in range(20,26) for y in range(20,26)])
points15 = [(10,3),(4,9),(8,10),(13,9),(14,11),(2,15)]
points50 = [(10, 10),(20,20),(30, 0),(30, 40),(50, 40)]
points50b = set()
for i in range(1000):
	points50b.add((randint(0,50),randint(0,50)))


points = points50b


def search(points, k, c):
    solution = localSearch(RechercheLocale(points), k, c)
    return [(x,y,r) for (x,y,r,list) in solution]



class RechercheLocale(State):
    def __init__(self,points):
        self.antennas = [(x, y, 1, [(x, y)]) for (x,y) in points]


print '**************************************************************************'
print 'Julien et Abdelhadi sont fiers de vous presenter leur nouvel algorithme :3'
print '**************************************************************************'
start = time.time()
solution = search(points, K, C)
end = time.time()
print '**************************************************************************'
print str(solution)
print '**************************************************************************'
# print '*******************************'
print '*************** En seulement {} seconds :D ****************'.format(end-start)
print '**************************************************************************'
# print '*******************************'

root = tk.Tk()
canvas = tk.Canvas(root, width=15*grille[0], height=15*grille[1], borderwidth=1, highlightthickness=0, bg="white")
canvas.grid()
nb = 0

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

for i in range(grille[0]):
    canvas.create_line(15 * i, 0, 15 * i, 15*grille[0])
    canvas.create_line(0, 15 * i, 15*grille[1], 15 * i)
for (x,y) in points:
	nb += 1
	canvas.create_circle(x*15,(grille[0]-y)*15,4,fill="red",outline="red")
for (x,y,r) in solution:
	canvas.create_circle(x*15,(grille[0]-y)*15,r*15)
	canvas.create_circle(x*15,(grille[0]-y)*15,2,fill="black")

print str(nb) + ' points'
sortie = raw_input("Appuyez sur une touche pour quitter")



