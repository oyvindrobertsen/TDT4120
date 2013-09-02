from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None
    dybde = None
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.dybde = -1
        self.ratatosk = False
        self.nesteBarn = 0


def dfs(rot):
    rot.dybde = 0
    stack = [rot]
    while stack:
        cur = stack.pop()
        if cur.ratatosk:
            return cur.dybde
        while cur.barn:
            cur.barn[len(cur.barn)-1].dybde = cur.dybde + 1
            stack.append(cur.barn.pop())


def bfs(rot):
    rot.dybde = 0
    queue = deque([rot]) 
    while queue:
        p = queue.popleft()
        if p.ratatosk:
            return p.dybde
        for i in xrange(len(p.barn)):
            p.barn[i].dybde = p.dybde + 1
            queue.append(p.barn[i])


def main():
    funksjon = stdin.readline().strip()
    antall_noder = int(stdin.readline())
    noder = []
    for i in range(antall_noder):
        noder.append(Node())
    start_node = noder[int(stdin.readline())]
    ratatosk_node = noder[int(stdin.readline())]
    ratatosk_node.ratatosk = True
    for linje in stdin:
        tall = linje.split()
        temp_node = noder[int(tall.pop(0))]
        for barn_nr in tall:
            temp_node.barn.append(noder[int(barn_nr)])

    if funksjon == 'dfs':
        print dfs(start_node)
    elif funksjon == 'bfs':
        print bfs(start_node)
    elif funksjon == 'velg':
       return

main()
