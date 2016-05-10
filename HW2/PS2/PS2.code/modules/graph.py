from random import shuffle
from math import floor
from ID3 import *
from operator import xor
from parse import parse
import matplotlib.pyplot as plt
import os.path
from pruning import validation_accuracy

# NOTE: these functions are just for your reference, you will NOT be graded on their output
# so you can feel free to implement them as you choose, or not implement them at all if you want
# to use an entirely different method for graphing

def get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, pct, depth):
    '''
    get_graph_accuracy_partial - Given a PARTIAL training set, attribute metadata, validation set, numerical splits count, and percentage,
    this function will return the validation accuracy of a specified (percentage) portion of the trainging setself.
    '''
    #depth = 'limit_depth'    
    tree = ID3(train_set, attribute_metadata, numerical_splits_count, depth) 
    print "splits counts after one iter: " + str(numerical_splits_count) 
    return validation_accuracy(tree, validate_set)

def get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, iterations, pcts, depth):
    '''
    Given a FULL training set, attribute metadata, validation set, numerical splits count, iterations, and percentages,
    this function will return an array of the averaged graph accuracy partials based off the number of iterations.
    '''
    partial_set= []
    avg_set = [] 
    for x in range(len(pcts)):
        subset_size = math.floor(pcts[x]*len(train_set))
        print"subset_size: " + str(subset_size)
        SUM = 0 
        counts = 0
        for iters in range(iterations):
            shuffle(train_set)
            for index in range(int(subset_size)):
                partial_set.append(train_set[index])
            #print "partial set:" + str(partial_set)
            acc = get_graph_accuracy_partial(partial_set, attribute_metadata, validate_set, numerical_splits_count, pcts[x], depth)
            SUM = SUM + acc
            #print "accuracy: " + str(acc) 
            numerical_splits_count = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
            counts = counts + 1            
            partial_set = []
        avg_set.append(SUM/float(counts))
    print "avg_set: " + str(avg_set)
    return avg_set
            

# get_graph will plot the points of the results from get_graph_data and return a graph
def get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment):
    '''
    get_graph - Given a training set, attribute metadata, validation set, numerical splits count, depth, iterations, lower(range),
    upper(range), and increment, this function will graph the results from get_graph_data in reference to the drange
    percentages of the data.
    '''
    pcts = []
    thing = lower
    while thing <= upper:
        pcts.append(thing) 
        thing = thing + increment
    print "Pcts: "+ str(pcts)
    
    accs = get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, iterations, pcts, depth)
    
    plt.plot(pcts,accs)
    plt.title('Learning Curve')
    plt.ylabel('Percent Correct on Test Set')
    plt.xlabel('Fraction of Training Set Used')
    plt.show()