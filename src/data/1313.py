import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10**9 + 7


class LowestCommonAncestor:
    """木のLCAを求める。構築：O(NlogN),クエリ：O(logN)"""
    def __init__(self, G, root=0):
        """
        :param G: 木の隣接リスト。[(コスト,頂点),(コスト,頂点)…]の形で渡す
        :param root: 木の根
        """
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.dist = [0] * self.n  # dist[v]:根からvの距離
        self.depth = [-1 if i != root else 0
                      for i in range(self.n)]  # depth[v]:頂点vの深さ
        self.parent = [[-1] * self.n
                       for _ in range(self.logn)]  # parent[k][v]:頂点vの2^k先の親
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for cost, v in self.G[u]:
                if self.depth[v] == -1:
                    self.dist[v] = self.dist[u] + cost
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i -
                                                                       1][v]]

    def get_lca(self, u, v):
        """uとvのLCAをO(logN)で求める"""
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        # LCAまでの距離を同じにする
        du, dv = self.depth[u], self.depth[v]
        for i in range(self.logn):
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        # 二分探索でLCAを求める
        if u == v:
            return u
        for i in range(self.logn - 1, -1, -1):
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

    def get_dist(self, u, v):
        """uとvの距離をO(logN)で求める"""
        r = self.get_lca(u, v)
        return (self.dist[u] - self.dist[r]) + (self.dist[v] - self.dist[r])


def solve():
    n, q = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append([1, b])
        edge[b].append([1, a])
    lca = LowestCommonAncestor(edge)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        d = lca.get_dist(c, d)
        if d % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    solve()
