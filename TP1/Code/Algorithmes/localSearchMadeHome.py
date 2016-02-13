__author__ = 'juanta'

from copy import deepcopy
from math import *

def dist(p1,p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def barycentre(points):
    x = 0
    y = 0
    n = len(points)
    for (xp, yp) in points:
        x += xp
        y += yp
    return (x/n,y/n)

def localSearch(initialState, K, C):
        ants = deepcopy(initialState.antennas)
        while len(ants) > 1:
            (x,y,r, liste1) = ants.pop()
            fusion = False
            # print 'antennas : ' + str(initialState.antennas)
            # print 'ants : ' + str(ants)
            for (x2, y2, r2, liste2) in ants:
                cout = 2*K + C*(r**2 + r2**2)
                bar = barycentre(liste1 + liste2)
                newR = 0
                for p in liste1 + liste2:
                    d = dist(bar, p)
                    if d > newR:
                        newR = d
                newR = int(ceil(newR))
                # print 'Tentative de fusion des antennes ' + str((x, y, r)) + ' et ' + str((x2, y2, r2)) + ' en ' + str((bar,newR))
                # print str(cout) + '  ' + str(K + C*newR**2)
                    # int(ceil(dist((x,y),(x2,y2))/2))
                if K + C*newR**2 < cout:
                    fusion = True
                    ants.append((bar[0], bar[1], newR, liste1 + liste2))
                    # print '  --> Fusion des antennes ' + str((x, y, r)) + ' et ' + str((x2, y2, r2)) + ' en ' + str((int((x+x2)/2),int((y+y2)/2),newR))
                    initialState.antennas.append((bar[0], bar[1], newR, liste1 + liste2))
                    initialState.antennas.remove((x2,y2,r2, liste2))
                    initialState.antennas.remove((x,y,r, liste1))
                    ants.remove((x2,y2,r2, liste2))
                    break
        for (x,y,r,pointsCouverts) in initialState.antennas:
            maxDist = max(dist((x,y),p) for p in pointsCouverts)
            improvement = False
            for dx in range(-5,5):
                for dy in range(-5,5):
                    maxDistNew = max(dist((x+dx,y+dy),p) for p in pointsCouverts)
                    if maxDistNew < maxDist:
                        maxDist = maxDistNew
                        dX = dx
                        dY = dy
                        improvement = True
            if improvement:
                initialState.antennas.remove((x,y,r,pointsCouverts))
                initialState.antennas.append((x+dX,y+dY,int(ceil(maxDist)),pointsCouverts))



        return initialState.antennas
