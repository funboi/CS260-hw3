
from time import time
import requests as r

class Node():

    """ Node class to represent the nodes of the Trie """

    def __init__( self, val='' ):
        self.val = val
        self.child = {}


class Trie():

    """ Trie class """

    # Constructor
    def __init__(self):
        self.root = Node( '*' )
        self.nodeCount = 0

    # Reset the Trie
    def MAKENULL(self):
        self.root = Node()

    # Return the number of nodes 
    def GETCOUNT(self):
        return self.nodeCount

    # Insert words into the Trie
    def INSERT(self, word):
        node = self.root
        word += '$'
        for c in word:
            if (c not in node.child):
                self.nodeCount += 1
                node.child[c] = Node(c)
            node = node.child[c]


def test( num_nodes: int ):

    start = time()
    assert num_nodes == 24358, "Inserting words into Trie failed"
    end = time()
    t = ( end - start ) * 1000

    print ( "Completed testing insert() into Trie in %f ms" % t )
    

if __name__ == "__main__":
    
    #Create Trie
    T = Trie()

    #Read from file and insert words into trie
    with open( 'alice30.txt' ) as f:
        for line in f:
                wordList = line.split(' ')
                for word in wordList:
                    
                    T.INSERT(word)

    trieNodes = T.GETCOUNT()

    # ---------------- Display the result

    print( "\n---------------- Trie Implementation ----------------\n" )
    print( "Total number of Trie Nodes: " + str( trieNodes ) )

    # ---------------- Test Trie Insertion

    test( trieNodes )