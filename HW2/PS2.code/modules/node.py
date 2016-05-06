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
                return self.children[instance[self.decision_attribute]].classify(instance)
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
        pass

def check_classify():
	n0 = Node()
	n0.label = 1
	i = 0;
	if n0.classify([0, 1, 2]) == 1:
		print "Passed 1"
		i += 1
	else:
		print "Failed 1"
	n1 = Node()
	n1.label = 0
	n = Node()
	n.label = None
	n.decision_attribute = 1
	n.is_nominal = True
	n.name = "You saw the attributes what do you think?"
	n.children = {1: n0, 2: n1}
	if n.classify([0, 2]) == 0:
		print "Passed 2"
		i += 1
	else:
		print "Failed 2"
        nN = Node()
        nN.decision_attribute = 3
        nN.is_nominal = False
        nN.name = "There is more to life than attributes"
        nN.children = [n1, n]
        nN.splitting_value = 75.0
        if nN.classify([0, 1, 0, 81.7]) == 1:
        	print "Passed 3"
                i += 1
        else:
		print "Failed 3"
	if i == 3:
		print "All tests passed"
	else:
		print "Not all tests passed, look at classify"

#check_classify()