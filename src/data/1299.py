import sys

input = sys.stdin.readline


class LCA:
    def __init__(self, G, root):
        V = len(G)
        self.log = 0
        while 2**self.log <= V:
            self.log += 1

        self.parent = [[-1] * V for _ in range(self.log)]
        self.depth = [0] * V
        stack = [root]
        while stack:
            v = stack.pop()
            p = self.parent[0][v]
            for c in G[v]:
                if c != p:
                    self.parent[0][c] = v
                    self.depth[c] = self.depth[v] + 1
                    stack.append(c)

        for k in range(self.log - 1):
            for v in range(V):
                if self.parent[k][v] >= 0:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        # go up to the same depth
        for k in range(self.log):
            if (self.depth[v] - self.depth[u]) >> k & 1:
                v = self.parent[k][v]
        if u == v:
            return u

        for k in range(self.log)[::-1]:
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)
lca = LCA(G, 0)
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if lca.dist(c, d) % 2 == 0:
        print("Town")
    else:
        print("Road")
