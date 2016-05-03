import math
from node import Node
import sys
from collections import defaultdict

def ID3(data_set, attribute_metadata, numerical_splits_count, depth):
    '''
    See Textbook for algorithm.
    Make sure to handle unknown values, some suggested approaches were
    given in lecture.
    ========================================================================================================
    Input:  A data_set, attribute_metadata, maximum number of splits to consider for numerical attributes,
	maximum depth to search to (depth = 0 indicates that this node should output a label)
    ========================================================================================================
    Output: The node representing the decision tree learned over the given data set
    ========================================================================================================

    '''
    # Your code here
    pass

def check_homogenous(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Checks if the attribute at index 0 is the same for the data_set, if so return output otherwise None.
    ========================================================================================================
    Output: Return either the homogenous attribute or None
    ========================================================================================================
    '''
    count = 0    
    for index in range(len(data_set)-1):
        if data_set[index][0] is data_set[index + 1][0]:
            count = count + 1    
    if count is (len(data_set)-1):       
        return data_set[0][0]
    else:
        return
        
# ======== Test Cases =============================
#data_set = [[0],[1],[1],[1],[1],[1]]
#print check_homogenous(data_set) == None
#data_set = [[0],[1],[None],[0]]
#print check_homogenous(data_set) ==  None
#data_set = [[1],[1],[1],[1],[1],[1]]
#print check_homogenous(data_set) ==  1


def pick_best_attribute(data_set, attribute_metadata, numerical_splits_count):
    '''
    ========================================================================================================
    Input:  A data_set, attribute_metadata, splits counts for numeric
    ========================================================================================================
    Job:    Find the attribute that maximizes the gain ratio. If attribute is numeric return best split value.
            If nominal, then split value is False.
            If gain ratio of all the attributes is 0, then return False, False
            Only consider numeric splits for which numerical_splits_count is greater than zero
    ========================================================================================================
    Output: best attribute, split value if numeric
    ========================================================================================================
    '''
    # Your code here
    pass

# # ======== Test Cases =============================
# numerical_splits_count = [20,20]
# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
# data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)
# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
# data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)

# Uses gain_ratio_nominal or gain_ratio_numeric to calculate gain ratio.

def mode(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Takes a data_set and finds mode of index 0.
    ========================================================================================================
    Output: mode of index 0.
    ========================================================================================================
    '''
    count_1 = 0
    count_0 = 0    
    for index in range(len(data_set)):
        if data_set[index][0] is 1:
            count_1 = count_1 + 1
        if data_set[index][0] is 0:
            count_0 = count_0 + 1
    if count_1 >= count_0:
        return 1
    else:
        return 0 
    
# ======== Test case =============================
#data_set = [[0],[1],[1],[1],[1],[1]]
#print mode(data_set) == 1
#data_set = [[0],[1],[0],[0]]
#print mode(data_set) == 0

def entropy(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Calculates the entropy of the attribute at the 0th index, the value we want to predict.
    ========================================================================================================
    Output: Returns entropy. See Textbook for formula
    ========================================================================================================
    '''
    Nm = len(data_set)
    Nm_1 = 0
    Nm_0 = 0
    for index in range(Nm):
        if data_set[index][0] is 1:
            Nm_1 = Nm_1 + 1 
        elif data_set[index][0] is 0:
            Nm_0= Nm_0 + 1 
    P1 = Nm_1/float(Nm)
    P2 = Nm_0/float(Nm)
    if P1 <= 0:
        P1 = 1
    if P2 <= 0:
        P2 = 1
    return -P1*math.log(P1,2)+ -P2*math.log(P2,2)
   
   # are these always binary?

# ======== Test case =============================
#data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
#print entropy(data_set) == 0.811
#data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
#print entropy(data_set) == 1.0
#data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
#print entropy(data_set) == 0

def split_on_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  subset of data set, the index for a nominal attribute.
    ========================================================================================================
    Job:    Creates a dictionary of all values of the attribute.
    ========================================================================================================
    Output: Dictionary of all values pointing to a list of all the data with that attribute
    ========================================================================================================
    '''
    
    dictionary= {}    
    for index in range (len(data_set)): 
         key = data_set[index][attribute]   
         dictionary.setdefault(key,[])            
         dictionary[key].append(data_set[index])
             
    return dictionary
    
# ======== Test case =============================
#data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
#print split_on_nominal(data_set, attr) == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}
#data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
#print split_on_nominal(data_set, attr) == {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}

def gain_ratio_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  Subset of data_set, index for a nominal attribute
    ========================================================================================================
    Job:    Finds the gain ratio of a nominal attribute in relation to the variable we are training on.
    ========================================================================================================
    Output: Returns gain_ratio. See https://en.wikipedia.org/wiki/Information_gain_ratio
    ========================================================================================================
    '''
    # getting the highest valued atrribute to look for    
    attr_max = 0
    for i in range(len(data_set)):
        if data_set[i][attribute] > attr_max:
            attr_max = data_set[i][attribute]
   
    # creating the new ordered data set        
    new_data_set = []
    new_data_set_temp = []
    for attr in range(attr_max+1):
        for j in range(len(data_set)):
            if data_set[j][attribute] is attr:
                new_data_set_temp.append(data_set[j])
        if len(new_data_set_temp) > 0:
            new_data_set.append(new_data_set_temp)
        new_data_set_temp = []

    # calculating gain ratio 
    SUM_IG = 0.0  
    SUM_IV = 0.0
    length = len(new_data_set)
    for index in range (length):
        ratio= len(new_data_set[index])/float(len(data_set))
        SUM_IG = SUM_IG + ratio*entropy(new_data_set[index])
        SUM_IV = SUM_IV + ratio*math.log(ratio, 2)
    IG =  entropy(data_set) - SUM_IG
    IV = -SUM_IV
    return IG/IV
    
    
# ======== Test case =============================
#data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
#print gain_ratio_nominal(data_set,attr)== 0.11470666361703151
#data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
#print gain_ratio_nominal(data_set,attr)== 0.2056423328155741
#data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
#print gain_ratio_nominal(data_set,attr)== 0.06409559743967516

def split_on_numerical(data_set, attribute, splitting_value):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, threshold (splitting) value
    ========================================================================================================
    Job:    Splits data_set into a tuple of two lists, the first list contains the examples where the given
	attribute has value less than the splitting value, the second list contains the other examples
    ========================================================================================================
    Output: Tuple of two lists as described above
    ========================================================================================================
    '''
    less= []
    more= []    
    for index in range (len(data_set)):
        if data_set[index][attribute] < splitting_value: 
            less.append(data_set[index])
        elif data_set[index][attribute] >= splitting_value: 
            more.append(data_set[index])
    return (less, more)
    
# ======== Test case =============================
#d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48
#print split_on_numerical(d_set,a,sval) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])
#d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
#print split_on_numerical(d_set,a,sval) == ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]])

def gain_ratio_numeric(data_set, attribute, steps):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, and a step size for normalizing the data.
    ========================================================================================================
    Job:    Calculate the gain_ratio_numeric and find the best single threshold value
            The threshold will be used to split examples into two sets
                 those with attribute value GREATER THAN OR EQUAL TO threshold
                 those with attribute value LESS THAN threshold
            Use the equation here: https://en.wikipedia.org/wiki/Information_gain_ratio
            And restrict your search for possible thresholds to examples with array index mod(step) == 0
    ========================================================================================================
    Output: This function returns the gain ratio and threshold value
    ========================================================================================================
    '''
    best = 0
    threshold = 0
    index= 0
    
    while index <  len(data_set):
        new_data_set = split_on_numerical(data_set, attribute, data_set[index][attribute])
        
        # calculating gain ratio 
        SUM_IG = 0.0  
        SUM_IV = 0.0
       
        for i in range (0,2):
            if len(new_data_set[i]) is 0:
                SUM_IG = 0
                SUM_IV = -1
            else:
                ratio= len(new_data_set[i])/float(len(data_set))
                SUM_IG = SUM_IG + ratio*entropy(new_data_set[i])
                SUM_IV = SUM_IV + ratio*math.log(ratio, 2)
        IG =  entropy(data_set) - SUM_IG
        IV = -SUM_IV
        if IG/IV > best:
            best = IG/IV
            threshold = data_set[index][attribute]
        index = index + steps

    return(best, threshold)
        
        
# ======== Test case =============================
data_set,attr,step = [[0,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
gain_ratio_numeric(data_set,attr,step) 
#== (0.21744375685031775, 0.64)
data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
gain_ratio_numeric(data_set,attr,step) 
#== (0.11689800358692547, 0.94)
data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
gain_ratio_numeric(data_set,attr,step) 
#== (0.23645279766002802, 0.29)



