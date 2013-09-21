from sys import stdin
from gc import disable
disable()
def subgraphdensity(adjmat, startnode):
    n = len(adjmat)
    visited = {i: False for i in xrange(n)}
    vertices = 0
    edges = 0
    stack = [startnode]
    while stack:
        print stack, visited, vertices, edges
        vertices += 1
        cur = stack.pop()
        visited[cur] = True
        for i in xrange(n):
            if adjmat[cur][i] == 1 and not visited[i]:
                edges += 1
                stack.append(i)
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
