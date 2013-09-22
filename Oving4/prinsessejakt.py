from sys import stdin
from gc import disable
disable()
def subgraphdensity(adjmat, startnode):
    n = len(adjmat)
    visited = [False] * n
    vertices = 0
    edges = 0
    visited[startnode] = True
    stack = [startnode]
    while stack:
        cur = stack.pop()
        for i in xrange(n):
            if adjmat[cur][i] and not visited[i]:
                visited[i] = True
                stack.append(i)
    for i in xrange(n):
        if not visited[i]:
            vertices += 1
            for j in xrange(n):
                if adjmat[i][j] and not visited[j]:
                    edges += 1
    if vertices == 0:
        return 0.0
    else:
        return float(edges) / float(vertices**2)


def main():
    n = int(stdin.readline())
    adj = [None] * n # rows
    for i in range(0, n):
        adj[i] = [False] * n # collumns
        line = stdin.readline()
        for j in range(0, n):
            adj[i][j] = (line[j] == '1')
    for line in stdin:
        start = int(line)
        print "%.3f" % (subgraphdensity(adj, start) + 1E-12)
main()
