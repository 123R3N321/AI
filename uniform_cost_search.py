'''
This is an implementation of Dijkstra that follows exactly
as it goes in the AI textbook, mainly used to check homework
attempts

  first, we define each node as a list [cost, start, end]
  we put cost first as python sort and heapify could recognize that.

'''

global pathCosts, expandList, frontier, reached    # map stores city name as key, entire node with everything as value
pathCosts = []  # a list containing tups of city paths and costs
expandList = []
frontier = []
reached = {}

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

    def add_child(self, child, cost):   #add child, note we do not need to update parent info
        self.children.append(child)
        self.actionCosts.append(cost)

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.pathCost < other.pathCost

    def isGoal(self,goal):
        if self.name == goal.name:  #I prolly don even need name to name comparison cuz i have repr
            return True
        return False

'''
Now, the algorithm. We take
'''
def dijkstra(start, goal):   #pass in start and end and we dont even need graph cuz it is implied

    frontier.append(start)  # ofcourse we start from starting point
    iteration = 0
    while len(frontier) > 0 and iteration < 100000:    # repeated pop till we reach destination,
        node = heapq.heappop(frontier)

        if node.isGoal(goal):   #this happens right before we try to expand it
            return node
        traceExpand(node)   #this line simply records expansion order
        for child in Expand(node):
            if child not in reached or child.pathCost < (reached[child]).pathCost:
                reached[child] = child
                heapq.heappush(frontier, child)
            Trace(child) #first, scan once to remove old entry
                # tracePath(child)    #next, add new backtrack into record
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
        if node.children[i] not in reached:
            node.children[i].parent = node  # because a child could have multiple parents, we need to update here. (forward reachable != backward reachable)
            node.children[i].pathCost = node.pathCost + node.actionCosts[i] #update path cost of the children
        else:
            if node.children[i].pathCost+node.actionCosts[i] < node.children[i].pathCost:
                node.children[i].parent = node
                node.children[i].pathCost = node.pathCost + node.actionCosts[i]
                reached[node.children[i]] = node.children[i]
        yield node.children[i]

def tracePath(node):    #this traces entire branch backward and get pathcosts of each
    pathCosts.append((node.name, reached[node].pathCost))
    while node.parent:
        pathCosts.append((node.parent.name, node.parent.pathCost))
        node = node.parent


def Trace(node): # this func is called each time a child is explored
    for each in pathCosts:
        if each[0] == node.name:
            return
    tracePath(node)


def traceExpand(node):
    expandList.append(node.name)
    return node.name

def printTree(root):    #a depth-first print of entire tree
    for i in range(len(pathCosts)-1, -1, -1):
        if pathCosts[i][0] == root.name:
            print('\n')
        print(pathCosts[i], end=' ')


    #testcode section
# Create nodes for letters a to z
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
j = Node('j')
k = Node('k')
l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')
w = Node('w')
x = Node('x')
y = Node('y')
z = Node('z')


# now add parental links
r.add_child(s,80/2)
r.add_child(p,97/2)
r.add_child(c,146/2)
s.add_child(f,99)
s.add_child(a,140/2)
s.add_child(o,151)
p.add_child(b,101)
p.add_child(c,138)
c.add_child(d,120)
c.add_child(p,138)
c.add_child(d,120)
d.add_child(m,75)
m.add_child(l,70)
l.add_child(t,111)
a.add_child(t,118)
a.add_child(z,75)
z.add_child(o,71)
m.add_child(d,75)
f.add_child(b,211)
b.add_child(u,85)
b.add_child(g,90)
b.add_child(f,211)
u.add_child(h,98)




dijkstra(r, a)

print("pathTrace: ", printTree(r), "\n\n", "all expanded nodes: ", expandList)
