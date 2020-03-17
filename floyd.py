import numpy as np
from time import time

infty = 10**10

def floyd( adj_matrix: np.array, n: int ):

    """ Floyd's Algorithm with the option of recovering paths """

    i = j = k = 0

    # Initialize cost matrix and path matrix
    c = np.array( [[infty] * n] * n )
    p = np.array( [[infty] * n] * n )
    
    for i in range( n ):
        for j in range( n ):
            c[i,j] = adj_matrix[i,j]
            p[i,j] = 0
    

    # Set the diagonal of cost matrix to 0
    for i in range( n ):
        c[i,i] = 0
    

    # Find the shortest path between each nodes
    for k in range( n ):
        for i in range( n ):
            for j in range( n ):
                if c[i,k] + c[k,j] < c[i,j]:
                    c[i,j] = c[i,k] + c[k,j]
                    p[i,j] = k

    return c, p


def test( c: list, p: list ):

    """ Function to test Floyd's Algorithm """

    c_test = np.array([ [0,3,1,5,7,8],
                        [infty,0,infty,infty,infty,infty],
                        [infty,2,0,infty,infty,infty],
                        [infty,infty,infty,0,2,3],
                        [infty,infty,infty,infty,0,1],
                        [infty,infty,infty,infty,infty,0] ])


    p_test = np.array([ [0,2,0,0,3,4],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,4],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0] ])
    
    start = time()
    assert ( c_test == c ).all(), "Floyd's Algorithm failed"
    assert ( p_test == p ).all(), "Floyd's Algorithm failed"
    end = time()

    t = ( end - start ) * 1000
    print ( "\nCompleted Floyd's Algorithm test in %f ms\n" % t )

    

if __name__ == "__main__":

    # ---------------- Initialize Adjacency Matrix
    
    matrix = np.array([ [0,4,1,5,8,10], 
                        [infty,0,infty,infty,infty,infty], 
                        [infty,2,0,infty,infty,infty], 
                        [infty,infty,infty,0,2,infty],
                        [infty,infty,infty,infty,0,1],
                        [infty,infty,infty,infty,infty,0] ])

    n = len( matrix )  

    # ---------------- Display the shortest from each node to other

    print( " \n--------------- Floyd's Algorithm with the option of recovering paths ---------------\n " )

    A, P = floyd( matrix, n ) 

    print ( "Shortest Distance Matrix" )
    print (A)

    print ()

    print ( "Predecessor Matrix" )
    print (P)
    

    # ---------------- Test Floyd's Algorithm
    test( A, P )




