import queue

class Node:
    def __init__(self, color = []):   #when a Node is created, it only has its own name.
        self.color = color
        self.neighbors = []  # list containing other nodes

def ac3(pair):
    theQ = queue.Queue()
    theQ.put(pair)
    while not theQ.empty():
        node1, node2 = theQ.pop()
        if revise(node1, node2):
            if len(node1.color) == 0:
                return False
            for eachNode in node1.neighbors:
                theQ.put((eachNode, node1))
    return True

def revise(node1, node2):
    revised = False
    for eachColor in node1.color:
        if len(node2.color) == 1 and node2.color[0] == eachColor:
            node1.color.remove(eachColor)
            revised = True
    return revised

