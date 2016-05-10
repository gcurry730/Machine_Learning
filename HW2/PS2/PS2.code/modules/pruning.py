from node import Node
from ID3 import *
from operator import xor
from copy import deepcopy


# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def validation_accuracy(tree,validation_set):
    '''
    takes a tree and a validation set and returns the accuracy of the set on the given tree
    '''
    count = 0
    total = 0
    for x in validation_set:
        total = total + 1
        if tree.classify(x) == x[0]: 
            count = count + 1
    return count/float(total)

def delete_node(node):
    
    #make a deep copy of original
    original_node = deepcopy(node)    
    
    node.children = None
    node.decision_attribute = None
    node.label = node.mode
    #print "label changed to: " + str(node.mode)
    node.name = None
    node.is_nominal = None
    node.splitting_value = None
    node.pruned= True
    #node.mode = mode(data_set)
    
    return original_node
    
        
array = []

def traverse(root, parent):     
    #traverse until we find a label = 0 or 1 which hasn't been pruned
    if root.label is not (0): 
        if root.label is not (1):
            #print "label is: " + str(root.label)
    #        if root.pruned is (False or None):
    #            print "pruned?: " + str(root.pruned)
            if root.is_nominal:
                for key, value in root.children.iteritems():
                    parent = root
                    traverse(root.children[key], parent)
            else:     
                for index in range(len(root.children)):
                    if root.children[index] is not None:
                        parent = root
                        traverse(root.children[index], parent)
     
    #print "parent is: " + str(parent)
    if parent is not None: 
        if parent.pruned is None: 
            array.append(parent)               
    #print array                   
    return array
               
    
    
def restore_node(node_to_restore, original_node):
    node_to_restore.children = original_node.children
    node_to_restore.decision_attribute = original_node.decision_attribute
    node_to_restore.label = original_node.label
    node_to_restore.is_nominal = original_node.is_nominal
    node_to_restore.splitting_value = original_node.splitting_value
    # keep pruned to True
    return node_to_restore

    

def reduced_error_pruning(root,training_set,validation_set):
    '''
    take the a node, training set, and validation set and returns the improved node.
    You can implement this as you choose, but the goal is to remove some nodes such that doing so improves validation accuracy.
    NOTE you will probably not need to use the training set for your pruning strategy, but it's passed as an argument in the starter code just in case.
    '''    
    #calc initial accuracy
    best_acc= validation_accuracy(root, validation_set)
    for x in range(0, 7):
        # traverse until we find a label = 0 or 1 
        array_of_nodes = traverse(root, None)
        #print "array_of_nodes: " + str(array_of_nodes)
        
        for index in range (len(array_of_nodes)):       
            node_to_delete = array_of_nodes[index]
            #print "Node:" + str(node_to_delete)
            #print "Pruned?:" + str(node_to_delete.pruned)
        
            if node_to_delete.pruned is None:
                # delete a node & keep original copy 
                original_node = delete_node(node_to_delete)
                
                # calc new accuracy     
                new_acc= validation_accuracy(root, validation_set)  
                
                #print "initial accruracy is : " + str(initial_acc)
                print "accuracy after prune is: " + str(new_acc)
                
                if new_acc > best_acc:
                    print "this was a good prune!"
                    best_acc = new_acc
                else: 
                    #print "we restored to previous"
                    restore_node(node_to_delete, original_node)
                    #print "restored accuracy is: " + str(validation_accuracy(root, validation_set))
        print "best overall accuracy after " +str(x)+ "  loop is: " + str(best_acc)
        


