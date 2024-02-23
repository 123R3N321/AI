'''
This is an implementation of Dijkstra that follows exactly
as it goes in the AI textbook, mainly used to check homework
attempts

  first, we define each node as a list [cost, start, end]
  we put cost first as python sort and heapify could recognize that.

'''



import heapq
'''
Note that for now Nodes do not support math operation overload of any kind,
nor does it support re-branching and re-basing of giving one child to another
I will add these functionalities in the future.
'''
class Node:
    def __init__(self, name):   #when a Node is created, it only has its own name.
        self.name = name
        self.parent = None  #yes, we can have multiple parents, but each time we only recognize the best one as the parent
        self.children = []
        self.actionCosts = []   #it should know the costs to go to all children, when children added.
        self.pathCost = 0   #this will depend on its own parent if this node is added to a parent

    def add_child(self, childName, cost):   #create and add child together
        child = Node(childName)
        self.children.append(child)
        self.actionCosts.append(cost)
        child.parent = self
        child.pathCost = self.pathCost + cost  #essentially recursively defined; price builds up from grand grandpa, grandpa, parent...
        return child
    
    def __repr__(self):
        return self.name

    def isGoal(self,goal):
        if self.name == goal.name:  #I prolly don even need name to name comparison cuz i have repr
            return True
        return False

'''
Now, the algorithm. We take
'''
def dijkstra(start, goal):   #pass in start and end and we dont even need graph cuz it is implied
    frontier = []   # frontier start with empty list, stores all nodes
    reached = {}    # map stores city name as key, entire node with everything as value
    frontier.append(start)  # ofcourse we start from starting point
    iteration = 0
    while len(frontier) > 0 and iteration < 100000:    # repeated pop till we reach destination,
        node = heapq.heappop(frontier)

        if node.isGoal(goal):   #this happens right before we try to expand it
            return node

        for child in Expand(node):
            if child not in reached or child.pathCost < (reached[child]).pathCost:
                reached[child] = child
                heapq.heappush(frontier, child)
    raise Exception('Maximum computing depth of ',iteration,' reached, abort!')




'''
Now, the important part, is the Expand() function
which expands from a given node to its children
update path cost, and update the child's parent info

as a reminder:
All nodes that are explored, whether generated or expanded,
are reached. When a node is reached, it is definitely generated,
but not necessarily expanded yet; we say a node is expanded only
when (after) we find all its children, and these children are
said to be generated.
'''
def Expand(node):   # will also update parent info to be the best parent
    for i in range(len(node.children)): # using ind cuz we need reference to costs as well
        node.children[i].parent = node  # because a child could have multiple parents, we need to update here. (forward reachable != backward reachable)
        node.children[i].pathCost = node.pathCost + node.actionCosts[i] #update path cost of the children
        yield node.children[i]



    #testcode section
city1 = Node('City1')
city2 = city1.add_child('city2',100)
city3 = city2.add_child('city3',50)
city4 = city1.add_child('city4',70)
city5 = city4.add_child('city5',6)
print(city5.parent)
