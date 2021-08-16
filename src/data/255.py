from collections import defaultdict


class Graph:
    def __init__(self, N):
        self.V = N
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u - 1].append(v - 1)
        self.graph[v - 1].append(u - 1)

    def findAllDistance(self):
        dist = [-1] * (self.V)
        dist[0] = 0
        queue = [0]
        while queue:
            node = queue.pop(0)
            for n in self.graph[node]:
                if dist[n] == -1:
                    dist[n] = 1 - dist[node]
                    queue.append(n)
        return dist


if __name__ == '__main__':
    N, Q = map(int, input().split(" "))
    g = Graph(N)
    out = []
    for i in range(N - 1):
        g.add_edge(*map(int, input().split(" ")))
    ret = g.findAllDistance()
    for i in range(Q):
        a, b = map(int, input().split(" "))
        if ret[a - 1] == ret[b - 1]: out.append("Town")
        else: out.append("Road")
    print(*out, sep="\n")
