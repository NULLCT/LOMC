import sys
from collections import deque


class LCA:
    def __init__(self, G, N, root):
        self.T = []
        self.FS = [-1] * N
        self.depth = [-1] * (N + 1)
        self.root = root
        self.depth[N] = float('inf')
        self.dfs(G, root)

        L = len(self.T)

        self.K = L.bit_length() - 1
        self.e = N
        self.pow2 = [1]
        self.mask = [x.bit_length() - 1 for x in range(L + 1)]
        for i in range(self.K):
            self.pow2.append(self.pow2[-1] * 2)
        self.ST = [[self.e] * (L) for i in range(self.K + 1)]
        self.ST[0] = self.T

        for i in reversed(range(L)):
            for k in range(1, self.K + 1):
                if L < i + self.pow2[k]:
                    break
                self.ST[k][i] = self.op(self.ST[k - 1][i],
                                        self.ST[k - 1][i + self.pow2[k - 1]])

    def op(self, a, b):
        return a if self.depth[a] < self.depth[b] else b

    def st_query(self, l, r):
        if l >= r:
            return self.e
        x = r - l
        t = self.mask[x]
        return self.op(self.ST[t][l], self.ST[t][r - self.pow2[t]])

    def lca(self, u, v):
        l, r = self.FS[u], self.FS[v]
        if l > r:
            l, r = r, l
        return self.st_query(l, r + 1)

    def dfs(self, G, s):
        stack = deque([(s, -1, 0)])
        while stack:
            v, p, d = stack.pop()
            if v < 0:
                self.T.append(~v)
                continue
            self.depth[v] = d
            self.FS[v] = len(self.T)
            self.T.append(v)
            for nv in G[v]:
                if nv == p:
                    continue
                stack.append((~v, v, d + 1))
                stack.append((nv, v, d + 1))

    def dist(self, u, v):
        p = self.lca(u, v)
        return self.depth[u] + self.depth[v] - self.depth[p] * 2


n, q = map(int, input().split())
G = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

lca = LCA(G, n, 0)
ans = []
for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if lca.dist(c, d) % 2:
        ans.append('Road')
    else:
        ans.append('Town')

print(*ans, sep='\n')
