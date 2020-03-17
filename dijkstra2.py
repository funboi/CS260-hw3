
''' 
Dijkstra's shortest paths algorithm with a partially ordered tree as a 
priority queue and linked adjacency lists as the representation of the graph. 
'''

import numpy as np
from time import time

max_val = 6
infty = 100

class Node():

    """ Node class to represent vertex of a graph """

    def __init__(self):
        self.value = None
        self.label = None
        self.next = None


class Graph():

    """ Graph class to represent adjacency matrix as a graph """

    def __init__(self):
        self.dist = None
        self.successors = None
        self.toPot = None


def swap( a: int, b: int, G: list, P: list ):

    """ Function to swap two elements of Partially Ordered Tree """

    # Swap elements
    temp = P[b]
    P[b] = P[a]
    P[a] = temp

    # Set the values of the PoT nodes of Graph
    G[P[a]].toPot = a-1
    G[P[b]].toPot = b-1


def priority( a: int, G: list, P: list ):

    """ Function to return the priority of a Partially Ordered Tree Node """

    return G[P[a]].dist

def bubble_up( a: int, G: list, P: list ):

    """ Function to push a new element up until the tree is partially ordered again """

    if (a > 1):
        if priority( a, G, P ) < priority( a//2, G, P ):
            swap( a, a//2, G, P )
            bubble_up( a//2, G, P )


def bubble_down( a: int, G: list, P: list, last: int ):

    """ Function to push a new element down until the tree is partially ordered again """

    child = 2*a
    if ( ( child < last ) and ( priority( child+1, G, P ) < priority( child, G, P ))):
        child += 1
    
    if ( ( child <= last ) and ( priority( a, G, P ) > priority( child, G, P ) ) ):
        swap( a, child, G, P )
        bubble_down( child, G, P ,last )


def initialize( G: list, P: list, pLast: int ):

    """ Function to initialize the required variables """

    # Set the values of each graph in G to starting values
    for i in range( 0, max_val ):
        G[i].dist = infty
        G[i].toPot = i+1
        P[i+1] = i

    # Set the distance between the first node to itself as 0
    G[0].dist = 0
    pLast = max_val


def dijkstra( G: list, P: list, pLast: int, n: int ):

    """ Dijkstra's Algorithm """


    u = Node()
    v = Node()
    # Initialize variables
    initialize( G, P, pLast )

    # Initialize distance matrix
    dist = [0] * n

    count = 1
    while( pLast >= 1 ):
        
        # Select the node whose corresponding tree node is at the root of the POT
        v = P[1]
        # Swap v with the current last node of the tree
        swap( 1, pLast, G, P )
        # Remove v
        pLast -= 1
        # Restore POT by bubbling down the node we just placed at the root
        bubble_down( 1, G, P, pLast )
        ps = G[v].successors

        while ( ps != None ):
            u = ps.value
            #print( str( count ) + " to " + str( u ) + ":"  )
            
            if( G[u-1].dist > G[v].dist + ps.label ):
                G[u-1].dist = G[v].dist + ps.label
                bubble_up( G[u-1].toPot, G, P )
            #print( str( G[u-1].dist ) )
            dist[u-1] = G[u-1].dist

            ps = ps.next

    return dist
        


def test( dist: list ):

    """ Function to test Dijkstra's Algorithm """

    start = time()
    assert dist == [0, 3, 1, 5, 7, 8], "Dijkstra's Algorithm failed"
    end = time()

    t = ( end - start ) * 1000

    print( "\nCompleted Dijkstra's Algorithm test in %f ms\n" % t )



if __name__ == '__main__':

    # ---------------- Initialize Graph

    num_nodes = 6

    A12 = Node()
    A12.value = 2
    A12.label = 4

    A13 = Node()
    A13.value = 3
    A13.label = 1

    A14 = Node()
    A14.value = 4
    A14.label = 5

    A15 = Node()
    A15.value = 5
    A15.label = 8

    A16 = Node()
    A16.value = 6
    A16.label = 10

    A32 = Node()
    A32.value = 2
    A32.label = 2

    A45 = Node()
    A45.value = 5
    A45.label = 2

    A56 = Node()
    A56.value = 6
    A56.label = 1

    graph = []
    for i in range( max_val ):
        graph.append( Graph() )

    graph[0].successors = A12
    A12.next = A13
    A13.next = A14
    A14.next = A15
    A15.next = A16
    A16.next = None

    graph[1].successors = None

    graph[2].successors = A32
    A32.next = None

    graph[3].successors = A45
    A45.next = None

    graph[4].successors = A56
    A56.next = None

    graph[5].successors = None


    # ---------------- Initialize Partially Ordered Tree

    potNodes = []
    for i in range( max_val+1 ):
        potNodes.append( Node() )

    # ---------------- Display the shortest path from the source to every other node

    print ( " \n--------------------- Dijkstra's Algorithm with a Partially Ordered Tree ---------------------\n" )
    
    print( "Vertex \t Distance from source" )
    dist = dijkstra( graph, potNodes, max_val, num_nodes )
    for i in range( len(dist) ):
        print ( "  %d \t\t %d" % ((i+1),dist[i]) )

    # ---------------- Test Dijkstra's Algorithm
    test( dist ) 

