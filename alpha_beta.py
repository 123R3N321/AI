'''
This is alphaBeta game algorithm
I think it is good cuz it can also be used to solve the stone game
from leetcode. Which is (kind of?) a popular technical interview problem
Assumptions and limitations include:
    assume 2 ply only (2 players)
    assume zero-sum game
    assume optimal moves (rational players)
    assume perfect information
    need manually log in game states (prolly the most painful part)
'''

'''
Analysis and thinking and scafolding of the program:
    It is essentially depth first search
    nodes have five attributes: type(min/max),score, alpha, beta, children
    we can havel multiple goals
'''

import math

class Node:
    def __init__(self, name, value, type):   #when a Node is created, it only has its own name.
        self.name = name
        self.value = value
        self.type = type
        self.parent = None  #yes, we can have multiple parents, but each time we only recognize the best one as the parent
        self.children = []
        self.alpha = -1 * math.inf
        self.beta = 1 * math.inf

    def add_child(self, child):   #add child, note we do not need to update parent info. Handled by algo
        self.children.append(child)

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value



