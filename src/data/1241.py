from collections import defaultdict

N, Q = map(int, input().split())
Edges = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edges[a].append(b)
    Edges[b].append(a)


class LCA():
    '''answer LCA queries for tree G.

        parameters:
            N:int
            G:tree(dict(list or set)), non-directed edges

        functions:
            get_lca:
                give two nodes x, y
                -> return LCA of x, y
            get_dist:
                give two nodes x,y
                -> return distance between x and y

        Examples:
            AOJ_GRL_5_C
            ABC_014_D
            etc...
    '''
    def __init__(self, N, G, root=0):
        if N == 1:
            return
        self.INF = N + 1
        self.dist = [self.INF] * N
        self.task = [(root, -1, 0)]
        self.P = [0] * N
        for v, p, d in self.task:
            self.dist[v] = d
            self.P[v] = p
            for e in G[v]:
                if e != p:
                    self.task.append((e, v, d + 1))
        self.md = self.task[-1][2]
        self.K = self.md.bit_length()
        self.L = [[0] * N for _ in range(self.K)]
        self.L[0] = [self.P[i] for i in range(N)]
        self.L[0][root] = root
        for i in range(1, self.K):
            for j in range(N):
                self.L[i][j] = self.L[i - 1][self.L[i - 1][j]]

    def get_lca(self, a, b):
        if N == 1:
            return a
        if self.dist[a] < self.dist[b]:
            a, b = b, a
        for j in range(self.K):
            if ((self.dist[a] - self.dist[b]) >> j) & 1:
                a = self.L[j][a]
        if a == b:
            return a
        for j in range(self.K - 1, -1, -1):
            if self.L[j][a] != self.L[j][b]:
                a = self.L[j][a]
                b = self.L[j][b]
        return self.L[0][a]

    def get_dist(self, a, b):
        if N == 1:
            return 0
        c = self.get_lca(a, b)
        return self.dist[a] + self.dist[b] - self.dist[c] * 2


lca = LCA(N, Edges)
S = ['Town', 'Road']
ans = []

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    v = lca.get_dist(c, d)
    ans.append(S[v % 2])

print(*ans, sep='\n')
