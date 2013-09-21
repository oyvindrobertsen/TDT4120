from sys import stdin
from gc import disable
disable()
def build(words):
    pos = 0
    root = ({}, [])
    for w in words:
        current = root
        for letter in w:
            children = current[0]
            if letter not in children:
                children[letter] = ({},[])
            current = children[letter]
        current[1].append(pos)
        pos += len(w) + 1
    return root
def positions(word, index, node):
    if index == len(word):
        return node[1]
    letter = word[index]
    if letter == '?':
        ret = []
        for value in node[0].values():
            ret += positions(word, index+1, value)
        return ret
    if letter not in node[0]:
        return []
    return positions(word, index+1, node[0][letter])
def main():
    s = stdin
    rootnode = build(s.readline().split())
    for searchterm in s:
        searchterm = searchterm.strip()
        pos = positions(searchterm, 0, rootnode)
        pos.sort()
        print searchterm + ':',
        for p in pos:
            print p,
        print

main()
