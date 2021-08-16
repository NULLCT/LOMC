import sys


class LCA:
    def __init__(self, n, e):
        self.n = n
        self.g = self._generate_adjacently_list(e)

        self.s = []
        self.f = [0] * n
        self.depth = [0] * n
        self.seen = [False] * n
        self._dfs(0, 0)

        self.INF = (self.n, None)

        self.m = 2 * self.n
        self.m0 = 2**(self.m - 1).bit_length()
        self.data = [self.INF] * (2 * self.m0)
        for i, v in enumerate(self.s):
            self.data[self.m0 - 1 + i] = (self.depth[v], i)
        for i in range(self.m0 - 2, -1, -1):
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def _generate_adjacently_list(self, e):
        g = [[] for _ in range(self.n)]
        for a, b in e:
            g[a].append(b)
            g[b].append(a)
        return g

    def _dfs(self, v, d):
        self.f[v] = len(self.s)
        self.depth[v] = d
        self.s.append(v)
        self.seen[v] = True
        for w in self.g[v]:
            if not self.seen[w]:
                self._dfs(w, d + 1)
                self.s.append(v)

    def _query(self, a, b):
        yield self.INF
        a += self.m0
        b += self.m0
        while a < b:
            if b & 1:
                b -= 1
                yield self.data[b - 1]
            if a & 1:
                yield self.data[a - 1]
                a += 1
            a >>= 1
            b >>= 1

    def query(self, u, v):
        fu = self.f[u]
        fv = self.f[v]
        if fu > fv:
            fu, fv = fv, fu
        return self.s[min(self._query(fu, fv + 1))[1]]

    def get_dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.query(u, v)]

    def is_on_path(self, u, v, a):
        return self.get_dist(u, a) + self.get_dist(a, v) == self.get_dist(u, v)


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)

    n, q = map(int, input().split())
    edges = [[int(i) - 1 for i in input().split()] for _ in range(n - 1)]

    lca = LCA(n, edges)

    ans = []
    for _ in range(q):
        c, d = map(lambda x: int(x) - 1, input().split())
        ans.append('Town' if lca.get_dist(c, d) % 2 == 0 else 'Road')

    print('\n'.join(ans))
