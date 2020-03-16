# !/usr/bin/env python3
# Author: Rayan Shrestha
# 3/16/2020
# CS-260 Section 007
# Programming Assignment 3

class Node():
    def __init__(self, val=''):
        self.val = val
        self.child = {}

#Trie class
class Trie():

    #Constructor
    def __init__(self):
        self.root = Node('*')
        self.nodeCount = 0

    #Trie becomes empty
    def MAKENULL(self):
        self.root = Node()

    #return count
    def GETCOUNT(self):
        return self.nodeCount

    #Inserts word into character
    def INSERT(self, word):
        node = self.root
        word += '$'
        for c in word:
            if (c not in node.child):
                self.nodeCount += 1
                node.child[c] = Node(c)
            node = node.child[c]


if __name__ == "__main__":
    #Create a trie
    T = Trie()

    #Read from file and insert words into trie
    F = open('alice30.txt', 'r')
    for line in F:
            wordList = line.split(' ')
            for word in wordList:
                T.INSERT(word)

    trieNodes = str(T.GETCOUNT())
    #Print out result
    print("\nTrie Implementation \n")
    print("Words Inserted from Alice in Wonderland")
    print("------------------------------------------------------")
    print("Total number of Trie Nodes: " + trieNodes)

