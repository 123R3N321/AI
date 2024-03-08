import heapq
from collections import defaultdict

#Data logged and tested by @Wea3el
#Algorithm developed by @123r3n321


global pathCosts, expandList, frontier, reached, hMap, weight    # map stores city name as key, entire node with everything as value
pathCosts = []  # a list containing tups of city paths and cost, and h cost
expandList = []
frontier = []
reached = {}
hMap = defaultdict(lambda: 99999)   #a huge default value for heuristic
weight = 1.0    #weight 1 gives standard astar algo.


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
        return self.pathCost + heuristic(self) < other.pathCost + heuristic(other)
        # return self.pathCost < other.pathCost

    def isGoal(self,goal):
        if self.name == goal.name:  #I prolly don even need name to name comparison cuz i have repr
            return True
        return False




def A_star(start, goal):
    frontier.append(start)  # ofcourse we start from starting point
    iteration = 0
    while len(frontier) > 0 and iteration < 100:  # repeated pop till we reach destination,
        iteration += 1
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


def Expand(node):
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

def heuristic(node):
    return weight * hMap[node.name]


def Trace(node): # this func is called each time a child is explored
    for each in pathCosts:
        if each[0] == node.name:
            return
    tracePath(node)

def traceExpand(node):
    expandList.append(node.name)
    return node.name

def tracePath(node):    #this traces entire branch backward and get pathcosts of each
    pathCosts.append((node.name, reached[node].pathCost, heuristic(node)))
    while node.parent and node.parent not in pathCosts:
        pathCosts.append((node.parent.name, node.parent.pathCost, heuristic(node.parent)))
        node = node.parent

def printTree(root):    #a depth-first print of entire tree
    for i in range(len(pathCosts)-1, -1, -1):
        if pathCosts[i][0] == root.name:
            print('\n')
        print(pathCosts[i], end=' ')







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


o.add_child(z,71)
o.add_child(s,151)
z.add_child(a,75)
a.add_child(s,140)
a.add_child(t,118)
t.add_child(l,111)
l.add_child(m,70)
m.add_child(d,75)
d.add_child(c,120)
s.add_child(r,80)
s.add_child(f,99)
r.add_child(c,146)
r.add_child(p,97)
c.add_child(p,138)
f.add_child(b,211)
p.add_child(b,101)


hMap['a']=366
hMap['b']=0
hMap['c']=160
hMap['d']=242
hMap['e']=161
hMap['f']=176
hMap['g']=77
hMap['h']=151
hMap['i']=226
hMap['l']=244
hMap['m']=241
hMap['n']=234
hMap['o']=380
hMap['p']=100
hMap['r']=193
hMap['s']=253
hMap['t']=329
hMap['u']=80
hMap['v']=199
hMap['z']=374


A_star(o, b)

print("pathTrace: ", printTree(r), "\n\n", "all expanded nodes: ", expandList)
