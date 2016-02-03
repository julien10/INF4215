# video.py
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca
# Date:   Januay 7th 2015
#
# This problem consists in selecting a set of videoa that cover a list of topics
# given as input, such that their total duration is minimized

import sys
sys.path.append('../Algorithmes')

from node import *
from state import *
from breadthfirst_search import *
from depthfirst_search import *
from lowestcost_search import *


db = {
       'v0':  {  'duration': 10,
                 'topics': set(['soccer']) },

       'v1':  {  'duration': 30,
                 'topics': set(['ski','hockey']) },

       'v2':  {  'duration': 50,
                 'topics': set(['soccer','ia','robots']) },
       
       'v3':  {  'duration': 40,
                 'topics': set(['infographie','dragons']) },

       'v4':  {  'duration': 50,
                 'topics': set(['ski','robots']) } }


class VideoState(State):
    def __init__(self,topics):
        self.uncoveredTopics = set(topics)
        self.chosenVideos = set()
        
    def equals(self,otherState):
        return ( self.chosenVideos == otherState.chosenVideos and
                 self.uncoveredTopics == otherState.uncoveredTopics)

    def show(self):
        print( self.chosenVideos, self.uncoveredTopics )

    def executeAction(self,action):
        (actionName, video) = action
        if actionName == 'add':
            self.chosenVideos.add(video)

            for t in db[video]['topics']:
                if t in self.uncoveredTopics:
                    self.uncoveredTopics.remove(t)

    def possibleActions(self):
        return [('add',v) for v in db.keys() if (v not in self.chosenVideos and
                                                 len(db[v]['topics'] & self.uncoveredTopics) > 0) ]
    
    def cost(self,action):
        (actionName, video) = action
        return db[video]['duration']

    def isGoal(self):
        return len(self.uncoveredTopics) == 0
    

solution = lowestcost_search(VideoState(['soccer','ski','robots']))

