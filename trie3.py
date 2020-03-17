import requests as r


class TrieNode( object ):
    def __init__( self, value: str = None ):
        
        super().__init__()
        #self.key = None
        self.value = None
        self.children = [None]*26


class Trie( object ):
    def __init__(self):
        
        super().__init__()
        self.root = TrieNode( "" )
        self.size = 0

    def insert( self, word: str ):

        current_word = word
        current_node = self.root

        if not current_word.isalpha():
            return
        
        

        while len( current_word ) > 0:
            
            current_letter = current_word[0].upper()
            
            if current_node.children[ord(current_letter) - 65] != None:
                current_node = current_node.children[ord(current_letter) - 65]
            
            else:
                new_node = TrieNode()
                new_node.value = current_letter
                current_node.children[ord(current_letter) - 65] = new_node
                current_node = new_node
                self.size += 1
            
            current_word = current_word[1:]

    def search( self, word ):
        
        current_word = word
        current_node = self.root

        while len( current_word ) > 0:

            current_letter = current_word[0]
            if current_node.children[ord(current_letter) - 65] != None:
                current_node = current_node.children[ord(current_letter) - 65]
                current_word = current_word[1:]
            else:
                return "Not in Trie"

        if current_node.value == None:
            return "None"

        return current_node.value

    
    def printTrie( self ):
        nodes = [ self.root ]
        while len( nodes ) > 0:
            for child in nodes[0].children:
                if child != None:
                    nodes.append(child)
            print (nodes.pop(0).value)
                


def makeTrie( words ):
    t = Trie()
    for word in words:
        t.insert( word )
    return t


if __name__ == "__main__":

    response = r.get( 'https://www.cs.drexel.edu/~knowak/cs260_winter_2020/alice30.txt' ).text
    p = response.split( ' ' )
    trie = makeTrie(p)
    #trie.printTrie()
    print (trie.size)
    