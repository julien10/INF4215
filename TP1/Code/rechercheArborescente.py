__author__ = 'Julien Antoine et Abdlhadi Temmar'



import sys
import time

from Algorithmes.breadthfirst_search import *
from Algorithmes.depthfirst_search import *
from Algorithmes.astar_search import *
from Algorithmes.branch_and_bound import *
from math import sqrt
import Tkinter as tk

grille = (50,50)
# grille = (30, 30)
K = 200
C = 1
initialUncoveredPoints = 0;
# points30 = [(10, 2),(8, 9),(23, 9),(14, 10), (29, 10), (17, 14), (4, 23), (28, 23), (29, 25), (17, 29)]
# points30 = [(10, 2),(8, 9), (29, 10), (4, 23), (29, 25), (17, 29)]    # points ecartes
points30 = [(10, 2),(8, 9), (29, 10), (23, 9), (14, 10), (17, 14)]      # points en haut
points15 = [(10,3),(4,9),(8,10),(13,9),(14,11),(2,15)]
points50 = [(10, 10),(20,20),(30, 0),(30, 40),(50, 40)]
points5 = [(1, 1),(2,2),(3, 0),(3, 4),(5, 4)]

points = points50


def search(points, k, c):
    K = k
    C = c
    return depthfirst_search(AntennaState(points))

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def densite(listPoints):
    if len(listPoints) == 0:
        return 1
    (minX, minY) = map(min, zip(*listPoints))
    (maxX, maxY) = map(max, zip(*listPoints))
    aire = (maxX - minX) * (maxY - minY)
    try:
        return float(len(listPoints))/aire
    except ZeroDivisionError:
        return 1


class AntennaState(State):

    def __init__(self,points):
        self.uncoveredPoints = set(points)
        self.antennas = set()
        self.initialUncoveredPoints = len(points)
        self.cout = 0

        (minX, minY) = map(min, zip(*points))
        (maxX, maxY) = map(max, zip(*points))
        maxDist = dist((minX, minY), (maxX, maxY)) / 2
        self.coutMax = 200 + (ceil(maxDist))**2

    # def equals(self,otherState):
    #     return ( self.chosenVideos == otherState.chosenVideos and
    #              self.uncoveredTopics == otherState.uncoveredTopics)

    def show(self):
        print( self.antennas, self.uncoveredPoints )

    def executeAction(self,action):
        (actionName, (x,y,r)) = action
        if actionName == 'add':
            self.antennas.add((x,y,r))
            self.cout += self.cost(action)
            listPoints = copy.deepcopy(self.uncoveredPoints)
            for p in listPoints:
                if dist(p,(x,y)) <= r:
                    self.uncoveredPoints.remove(p)

    def possibleActions(self):
        x = range(0,grille[0])
        y = range(0,grille[1])
        coordonnees = []
        if len(self.antennas) < self.initialUncoveredPoints and self.cout + K < self.coutMax :
            for xx in x:
                for yy in y:
                    for r in range(1,grille[0]/2 + 2):
                        if self.cout + K + C*r**2  > self.coutMax:
                            break
                        for (xPoint,yPoint) in self.uncoveredPoints:
                            distance = dist((xx,yy),(xPoint,yPoint)) - r
                            if distance >= -0.5 and distance <= 0:
                                coordonnees.append(('add',(xx,yy,r)))
        return coordonnees

    def cost(self,action):
        (actionName, (x,y,r)) = action
        return K + C*r**2

    def isGoal(self):
        return len(self.uncoveredPoints) == 0

    def heuristic(self):
        #print 1/densite(self.uncoveredPoints)/ (grille[0] * grille[1])
        return (1/densite(self.uncoveredPoints)) / (grille[0] * grille[1])
        # return maxDist(self)
        # return self.cout - self.coutMax

    # Calcule la distance entre les deux points les plus eloignes
    def maxDist(self):
        maxDist = 0
        listPoints = list(self.uncoveredPoints)
        for i in range(0, len(listPoints)):
            for j in range(i+1, len(listPoints)):
                maxDist = max(maxDist, dist(listPoints[i],listPoints[j]))
        return maxDist


start_time = time.time()

solution = search(points, 200, 1)
print str(solution.state.antennas)

#solution = branch_and_bound_search(AntennaState(points15))
# solution = astar_search(AntennaState(points30))
# solution = breadthfirst_search(AntennaState(points50))
# solution = lowestcost_search(AntennaState(points30))
# solution = depthfirst_search(AntennaState(points30))

print "Temps en secondes : " + str(time.time() - start_time)



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
    canvas.create_circle(x*15,(grille[0]-y)*15,3,fill="red",outline="red")
for (x,y,r) in solution.state.antennas:
    canvas.create_circle(x*15,(grille[0]-y)*15,r*15)
    canvas.create_circle(x*15,(grille[0]-y)*15,2,fill="black")

print str(nb) + ' points'
sortie = input("Appuyez sur une touche pour quitter")



