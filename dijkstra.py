
'''
Dijkstra's shortest paths algorithm with the 
adjacency matrix as the representation of the graph
'''


import numpy as np
from time import time

infty = 10**10


def dijkstra( adj_matrix: np.matrix, n: int ):

    """ Dijkstra's Algorithm """
    
    # Initialize Vertex inclusion Set 
    S = [0]
    D = np.array( [infty] * n )
    # Initialize distance Matrix
    dist = [0] * n

    # Initialize D
    for i in range( 1, n ):
        D[i] = adj_matrix.item( (0,i) )
    
    for i in range( n-1 ):
        
        # Choose a vertex w in V-S such that D[w] is minimum
        v_idx = D.argmin()
        # Add w to S
        S.append( v_idx )
        # Update the distance
        dist[v_idx] = D[v_idx]
        
        # Update the path 
        for k in range( len(D) ):
            D[k] = min( D[k], D[v_idx] + adj_matrix.item( (v_idx,k) ) )

        D[v_idx] = infty

    return dist


def test( dist: list ):

    """ Function to test Dijkstra's Algorithm """

    start = time()
    assert dist == [0, 3, 1, 5, 7, 8], "Dijkstra's Algorithm failed"
    end = time()

    t = ( end - start ) * 1000

    print( "\nCompleted Dijkstra's Algorithm test in %f ms\n" % t )


    
if __name__ == "__main__":
    
    # ---------------- Initialize Adjacency Matrix
    
    matrix = np.matrix([[0,4,1,5,8,10], 
                        [infty,0,infty,infty,infty,infty], 
                        [infty,2,0,infty,infty,infty], 
                        [infty,infty,infty,0,2,infty],
                        [infty,infty,infty,infty,0,1],
                        [infty,infty,infty,infty,infty,0]
                        ])

    num_nodes = len( matrix )

    # ---------------- Display the shortest path from the source to every other node

    print ( "\n--------------------- Dijkstra's Algorithm ---------------------\n" )

    print ( "Vertex \t Distance from source" )
    dist = dijkstra( matrix, num_nodes )
    for i in range( len(dist) ):
        print ( "  %d \t\t %d" % ((i+1),dist[i]) )
        #print (  )

    # ---------------- Test Dijkstra's Algorithm
    test( dist ) 



    

