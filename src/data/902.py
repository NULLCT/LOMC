import sys

sys.setrecursionlimit(10000000)


class LowestCommonAncedtor:
    def __init__(self, G, root):
        self.n = len(G)
        self.tour = [0] * (2 * self.n - 1)
        self.depth_list = [0] * (2 * self.n - 1)
        self.id = [0] * self.n
        self.visit_id = 0
        self.dfs(G, root, -1, 0)
        self._rmq_init(self.depth_list)

    def _rmq_init(self, arr):
        n = len(arr)
        self.N0 = 1 << (n - 1).bit_length()
        self.dat = [self.n] * (self.N0 - 1) + arr + [self.n
                                                     ] * (self.N0 - n + 1)
        self.index = [0] * (self.N0 - 1) + list(
            range(n)) + [0] * (self.N0 - n + 1)
        dat = self.dat
        index = self.index
        for i in range(self.N0 - 2, -1, -1):
            if dat[2 * i + 1] > dat[2 * i + 2]:
                dat[i] = dat[2 * i + 2]
                index[i] = index[2 * i + 2]
            else:
                dat[i] = dat[2 * i + 1]
                index[i] = index[2 * i + 1]

    def _rmq_query(self, l, r):
        """最小値となるindexを返す"""
        l += self.N0
        r += self.N0
        s = self.n
        dat = self.dat
        index = self.index
        while l < r:
            if r & 1:
                r -= 1
                if s > dat[r - 1]:
                    s = dat[r - 1]
                    res = index[r - 1]
            if l & 1:
                if s > dat[l - 1]:
                    s = dat[l - 1]
                    res = index[l - 1]
                l += 1
            l >>= 1
            r >>= 1
        return res

    def dfs(self, G, vertex, parent, depth):
        self.id[vertex] = self.visit_id
        self.tour[self.visit_id] = vertex
        self.depth_list[self.visit_id] = depth
        self.visit_id += 1
        for element in G[vertex]:
            if element != parent:
                self.dfs(G, element, vertex, depth + 1)
                self.tour[self.visit_id] = vertex
                self.depth_list[self.visit_id] = depth
                self.visit_id += 1

    def get(self, u, v):
        l, r = self.id[u], self.id[v]
        if r < l:
            l, r = r, l
        q = self._rmq_query(l, r + 1)
        return self.tour[q]

    def dist(self, u, v):
        """点u,点vの距離"""
        lca = self.get(u, v)
        depth_u = self.depth_list[self.id[u]]
        depth_v = self.depth_list[self.id[v]]
        depth_lca = self.depth_list[self.id[lca]]
        return depth_u + depth_v - 2 * depth_lca


#問.任意の2頂点の距離
n, q = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

lca = LowestCommonAncedtor(e, 0)
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if lca.dist(u, v) % 2 == 1:
        print("Road")
    else:
        print("Town")
