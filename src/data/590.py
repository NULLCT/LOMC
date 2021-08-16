# u, vの共通の親
# ダブリング p[i][v] = vの2^i個 親
# LevelAncestor(頂点vのh個親)
# LCA(Lowest common ansector)

from collections import deque


class lca():
    def __init__(self, n):
        self.n = n
        self.root = None
        self.edges = [[] for _ in range(n)]
        self.lv = n.bit_length()
        self.p = [[None] * n for _ in range(self.lv)]
        self.depth = [None] * n

    def set_root(self, root):
        self.root = root

    def add_edge(self, fm, to):
        self.edges[fm].append(to)

    def construct(self):
        # 深さと親の設定
        q = deque()
        q.append((self.root, 0))
        self.depth[self.root] = 0
        self.p[0][self.root] = 0
        while len(q) > 0:
            cur, dep = q.popleft()
            for nxt in self.edges[cur]:
                if self.p[0][nxt] != None: continue
                q.append((nxt, dep + 1))
                self.depth[nxt] = dep + 1
                self.p[0][nxt] = cur
        # ダブリング
        for i in range(1, self.lv):
            for v in range(self.n):
                self.p[i][v] = self.p[i - 1][self.p[i - 1][v]]

    def la(self, x, h):
        for i in range(self.lv)[::-1]:
            if h >= 1 << i:
                x = self.p[i][x]
                h -= 1 << i
        return x

    def lca(self, u, v):
        # u,vの高さを合わせる
        if self.depth[u] < self.depth[v]: u, v = v, u
        u = self.la(u, self.depth[u] - self.depth[v])
        if u == v: return u
        # u, vのギリギリ合わない高さまで昇る
        for i in range(self.lv)[::-1]:
            if self.p[i][u] != self.p[i][v]:
                u = self.p[i][u]
                v = self.p[i][v]
        return self.p[0][u]

    def dist(self, u, v):
        lca = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca]


n, q = map(int, input().split())

l = lca(n)
l.set_root(0)
for i in range(n - 1):
    a, b = map(int, input().split())
    l.add_edge(a - 1, b - 1)
    l.add_edge(b - 1, a - 1)
l.construct()

for i in range(q):
    x, y = map(int, input().split())
    d = l.dist(x - 1, y - 1)
    if d % 2 == 0:
        print('Town')
    else:
        print('Road')
