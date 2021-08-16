#
# LCA : Lowest Common Ancestor
#
import collections
import sys

sys.setrecursionlimit(10**6)


class LCA:
    def __init__(self, n, adj):
        K = 1
        while (1 << K) < n:
            K += 1
        self.parent = [[-1] * n for _ in range(K)]
        self.dist = [-1] * n
        self._dfs2(node=0, par=-1, d=0, adj=adj)
        for k in range(K - 1):
            for v in range(n):
                if self.parent[k][v] < 0:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def _dfs(self, node, par, d, adj):
        self.parent[0][node] = par
        self.dist[node] = d
        for nd in adj[node]:
            if nd == par: continue
            self._dfs(nd, node, d + 1, adj)

    def _dfs2(self, node, par, d, adj):
        s = [(node, par, d)]
        while s:
            node, par, d = s.pop()
            self.parent[0][node] = par
            self.dist[node] = d
            for nd in adj[node]:
                if nd == par: continue
                s.append((nd, node, d + 1))

    def query(self, u: int, v: int) -> int:
        if self.dist[u] < self.dist[v]: u, v = v, u
        K = len(self.parent)
        # LCA までの距離を同じにする
        for k in range(K):
            if (self.dist[u] - self.dist[v]) >> k & 1:
                u = self.parent[k][u]
        # 二分探索で LCA を求める
        if u == v: return u
        for k in range(K - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def distance(self, u: int, v: int) -> int:
        return self.dist[u] + self.dist[v] - 2 * self.dist[self.query(u, v)]

    def is_on_path(self, u, v, a) -> bool:
        return self.distance(u, a) + self.distance(a, v) == self.distance(u, v)


N, Q = map(int, input().split())
adj = collections.defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

lca = LCA(N, adj)
for _ in range(Q):
    c, d = map(int, input().split())
    if lca.distance(c - 1, d - 1) % 2 == 0:
        print('Town')
    else:
        print('Road')
