#from node import Node
import sys

path = [] 
def getPaths(root):
    '''
        returns a list of lists of nodes representing paths from root to leaf
    '''
    path.append(root)
   
    if root.label is not None:
        #print path
        makestring(path)
        print 'OR'
        path.pop()
    else:
        if root.is_nominal: 
            for key, value in root.children.iteritems():
                getPaths(root.children[key])
        else:
            for index in range(len(root.children)):
                getPaths(root.children[index])
        path.pop()

def makestring(path):
    '''
        prints conditional statements for the individual paths
    '''
    for index in range(len(path)):
        if path[index].label is None: 
            if path[index].is_nominal:
                                
                if len(path[index-1].children) > 0: 
                    for key, value in path[index-1].children.iteritems():
                        try:
                            if path[index-1].children[key] == path[index]:
                                print str(path[index].name) +' is key ' + str(key) + '...AND...'
                        except KeyError:
                            print str(path[index].name) +' is key ' + '...AND...'
                else:
                    print str(path[index].name) +' is key  ??'
            
            else: 
                if len(path[index-1].children) > 0:
                        try: 
                            if path[index-1].children[0] == path[index]:
                                print str(path[index].name) +' is less than ' +str(path[index].splitting_value) + '...AND...'
                            else: 
                                print str(path[index].name) +' is greater than ' +str(path[index].splitting_value) + ' ...AND...'
                        except KeyError:
                            print str(path[index].name) +' is greater than ' +str(path[index].splitting_value) + ' ...AND...'
                else:
                    print str(path[index].name) +' is less than ' +str(path[index].splitting_value) 
        else:
            if path[index].label is 1:
                print "Your team wins!"
            if path[index].label is 0:
                print "Your team loses."
