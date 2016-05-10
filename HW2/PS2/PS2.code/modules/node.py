# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 if numeric and a dictionary if nominal.  
#            For numeric, the 0 index holds examples < the splitting_value, the 
#            index holds examples >= the splitting value
#
# label - is None if there is a decision attribute, and is the output label (0 or 1 for
#	the homework data set) if there are no other attributes
#       to split on or the data is homogenous
#
# decision_attribute - the index of the decision attribute being split on
#
# is_nominal - is the decision attribute nominal
#
# value - Ignore (not used, output class if any goes in label)
#
# splitting_value - if numeric, where to split
#
# name - name of the attribute being split on
from modules.DNF import*

class Node:
    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        self.value = None
        self.splitting_value = None
        self.children = {}
        self.name = None
        self.mode = None
        #self.keys = None
        self.pruned = None
        self.avg = None

    def classify(self, instance):
        '''
        given a single observation, will return the output of the tree
        '''
        if self.label is 0:  
            return 0 
            
        elif self.label is 1:
            return 1
            
        else: 
            if self.is_nominal is True:
                try:
                    return self.children[instance[self.decision_attribute]].classify(instance)
                except KeyError:
                    return self.mode
                    print "I don't know how to classify this nominal example!"
                    print "My is_nominal is: " + str(self.is_nominal)
                    print str(instance[self.decision_attribute]) + " is not a good key"
                    print "my actual children are: " + str(self.children)
            
            if self.is_nominal is False:
                
                if instance[self.decision_attribute] >= self.splitting_value:
                    node= 1
                else:
                    node= 0
      
                return self.children[node].classify(instance)
    
    
    def print_tree(self, indent = 0):
        '''
        returns a string of the entire tree in human readable form
        '''
        # Your code here
        pass


    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        getPaths(self)
        
#=========TEST FOR DNF==================    
#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#n1 = Node()
#n1.name = 'n1'
#n1.label = None
#n1.is_nominal = False
#n1.decision_attribute = 1
#n1.splitting_value = 0.5
#
#n2 = Node()
#n2.name = 'n2'
#n2.label = 1
#
#n4 = Node()
#n4.name = 'n4'
#n4.label = 1
#
#n5 = Node()
#n5.name = 'n5'
#n5.label = 0
#
#n3 = Node()
#n3.name = 'n3'
#n3.label= None
#n3.is_nominal = False
#n3.decision_attribute = 1
#n3.splitting_value = 0.7
#
#n6 = Node()
#n6.name = 'n6'
#n6.label = 1
#
#n1.children = {0: n2, 1: n3, 2:n6}
#n3.children = {0: n4, 1: n5}
#
#getPaths(n1)
#n1.print_dnf_tree()

