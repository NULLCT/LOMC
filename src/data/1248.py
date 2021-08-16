class BinaryLiftingLCA:
    '''
    参考: https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
    '''
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, a, b):
        self.G[a].append(b)
        self.G[b].append(a)

    def from_graph(self, G):
        self.G = G

    def build(self, root=0):
        self.root = root
        self._bfs(root)
        self.maxdepth = max(self.d).bit_length()
        self.table = [self.prev]
        tmp1 = self.prev[:]
        for i in range(self.maxdepth):
            tmp2 = [0] * self.N
            for j in range(self.N):
                if tmp1[j] == -1: continue
                tmp2[j] = tmp1[tmp1[j]]
            self.table.append(tmp2)
            tmp1 = tmp2

    def lca(self, u, v):
        dd = self.d[v] - self.d[u]
        if dd < 0:
            u, v = v, u
            dd = -dd
        for k in range(self.maxdepth + 1):
            if dd & 1: v = self.table[k][v]
            dd >>= 1
        if u == v: return u
        for i in range(self.maxdepth - 1, -1, -1):
            pu = self.table[i][u]
            pv = self.table[i][v]
            if pu != pv:
                u = pu
                v = pv
        return self.table[self.root][u]

    def _bfs(self, s):
        from collections import deque
        seen = [0] * self.N
        self.d = [0] * self.N
        self.prev = [-1] * self.N
        todo = deque()
        seen[s] = 1
        todo.append(s)
        while len(todo):
            a = todo.popleft()
            for b in self.G[a]:
                if seen[b] == 0:
                    seen[b] = 1
                    todo.append(b)
                    self.d[b] += self.d[a] + 1
                    self.prev[b] = a


N, Q = map(int, input().split())
lca = BinaryLiftingLCA(N)
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    lca.add_edge(a, b)

lca.build()
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    w = lca.lca(c, d)
    dist = lca.d[c] + lca.d[d] - lca.d[w] * 2
    if dist % 2: print("Road")
    else: print("Town")
