# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - dictionary containing the children where the key is child number (1,...,k) and the value is the actual node object
# if node has no children, self.children = None
# value - value at the node
#
#
# The values for bfs should be returned as simply a string of value space value space value. For example if the tree looks like the following:
#     5
#   2   3
#
# The tree data structure is a node with value 5, with a dictionary of children {1: b, 2: c} where b is a node with value 2 and c is a node with value 3.  Both b and c have children of None.
# The bfs traversal of the above tree should return the string '5 2 3'

#import sys
#import os

class Node:
    def __init__(self):
        self.value = None
        self.children = None

    def get_value(self):
        return self.value

    def get_children(self):
        list = [self.children]
        return list

def get_child_string(root):
    list = ''
    if (root.children != None):
        length = len(root.children)
    else:
        length= 0
    i = 1
    while (i <= length ):
        list= list + str(root.children[i].get_value()) + ' '
        i = i+1
    return list

def breadth_first_search(root):
    list = str(root.value) +' ' + get_child_string(root)
    length = len(root.children)
    k=1
    while (root.children != None):
            j=1
            length= len(root.children)
            while (j <= length):
                list = list + get_child_string(root.children[j])
                j= j+1
            j=1
            root = root.children[j] # makes root D
            #k = k + 1
    return list

def tester():
    a = Node()
    a.value = 5
    b = Node()
    b.value = 7
    a.children = {1: b}
    c = Node()
    c.value = 1
    d = Node()
    d.value = 2
    e = Node()
    e.value = 3
    c.children = {1: d, 2: e}
    f = Node()
    f.value = 4
    g = Node()
    g.value = 5
    d.children= {1: f, 2: g}
    h = Node()
    h.value= 6
    i = Node()
    i.value= 7
    e.children = {1: h, 2: i}
    j = Node()
    j.value = 8
    k = Node()
    k.value = 9
    g.children = {1: j, 2:k}
    l = Node()
    l.value= 10
    i.children = {1: l}
    print str(a.get_value()) + ' should be 5.'
    print str(a.get_children()) + ' should be {1: ' + str(b) + '}.'
    print str(breadth_first_search(a)) + ' should be 5 7.'
    print str(breadth_first_search(c)) + ' should be 1 2 3 4 5 6 7 8 9 10'

    print str(get_child_string(c)) + ' should be 2 3'
    print str(get_child_string(d)) + ' should be 4 5'
    print str(get_child_string(e)) + ' should be 6 7'
    print str(get_child_string(f)) + ' should be  '
    print str(get_child_string(g)) + ' should be 8 9'
    print str(get_child_string(i)) + ' should be 10'


tester()