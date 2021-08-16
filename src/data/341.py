import sys

input = sys.stdin.readline
from collections import *


class LCA:
    def __init__(self, N, G):
        self.N = N
        self.G = G
        self.log_size = 22
        self.par = [[-1] * self.N for _ in range(self.log_size)]
        q = deque([0])
        self.dep = [-1] * self.N
        self.dep[0] = 0

        while q:
            v = q.popleft()

            for nv in self.G[v]:
                if self.dep[nv] == -1:
                    self.par[0][nv] = v
                    self.dep[nv] = self.dep[v] + 1
                    q.append(nv)

        for i in range(1, self.log_size):
            for v in range(self.N):
                if self.par[i - 1][v] >= 0:
                    self.par[i][v] = self.par[i - 1][self.par[i - 1][v]]

    def calc_lca(self, u, v):
        if self.dep[u] > self.dep[v]:
            u, v = v, u

        for i in range(self.log_size):
            if ((self.dep[v] - self.dep[u]) >> i) & 1:
                v = self.par[i][v]

        if u == v:
            return u

        for i in range(self.log_size - 1, -1, -1):
            if self.par[i][u] != self.par[i][v]:
                u, v = self.par[i][u], self.par[i][v]

        return self.par[0][u]

    def dist(self, u, v):
        return self.dep[u] + self.dep[v] - 2 * self.dep[self.calc_lca(u, v)]


N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

lca = LCA(N, G)

for _ in range(Q):
    c, d = map(int, input().split())
    dist = lca.dist(c - 1, d - 1)

    if dist % 2 == 0:
        print('Town')
    else:
        print('Road')
