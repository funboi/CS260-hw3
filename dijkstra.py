import numpy as np

infty = 10**10


def dijkstra( adj_matrix: np.matrix, n: int ):
    
    S = [0]
    D = np.array( [infty] * n )
    dist = [0] * n

    for i in range( 1, n ):
        D[i] = adj_matrix.item( (0,i) )
    
    for i in range( n-1 ):

        v_idx = D.argmin()
        S.append( v_idx )
        dist[v_idx] = D[v_idx]
        
        for k in range( len(D) ):
            D[k] = min( D[k], D[v_idx] + adj_matrix.item( (v_idx,k) ) )

        D[v_idx] = infty

    return D, dist
    
def main():

    # Initialize Adjacency Matrix
    matrix = np.matrix([[0,4,1,5,8,10], 
                        [infty,0,infty,infty,infty,infty], 
                        [infty,2,0,infty,infty,infty], 
                        [infty,infty,infty,0,2,infty],
                        [infty,infty,infty,infty,0,1],
                        [infty,infty,infty,infty,infty,0]
                        ])

    n = len( matrix )
    D, dist = dijkstra( matrix, n )

    print ( "Vertex \t Distance from Source" )
    for i in range( len(dist) ):
        print ( "%d \t\t %d" % (i, dist[i]))



if __name__ == "__main__":
    main()
    

