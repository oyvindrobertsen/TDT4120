from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.children = {}
        self.position = []

def build(wordlist):
    root = current = Node()
    for w in wordlist:
        for i in xrange(len(w[0])):
            curchar = w[0][i]
            if curchar in current.children:
                current = current.children[curchar]
            else:
                current.children[curchar] = Node()
                current = current.children[curchar]
            if i == len(w[0])-1:
                current.position.append(w[1])
        current = root
    return root

def positions(word, index, node):
    if index == len(word):
        return node.position
    letter = word[index]
    if letter == '?':
        ret = []
        for value in node.children.values():
            ret += positions(word, index+1, value)
        return ret
    if letter not in node.children:
        return []
    return positions(word, index+1, node.children[letter])


def printTree(node):
    for key in node.children.keys():
        print key, ':', node.children[key].position
        printTree(node.children[key])

try:
    words = stdin.readline().split()
    wordlist = []
    pos = 0
    for w in words:
        wordlist.append( (w,pos) )
        pos += len(w) + 1
    rootnode = build(wordlist)
    printTree(rootnode)
    for searchterm in stdin:
        searchterm = searchterm.strip()
        print searchterm + ":",
        pos = positions(searchterm, 0, rootnode)
        pos.sort()
        for p in pos:
            print p,
        print
except:
    traceback.print_exc(file=stderr)
