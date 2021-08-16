class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i -
                                                                       1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):  # depthの差分だけuを遡らせる
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v: return u  # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    G[x - 1] += [y - 1]
    G[y - 1] += [x - 1]

lca = LCA(G)
for _ in range(Q):
    c, d = map(int, input().split())
    common = lca.get(c - 1, d - 1)
    #頂点 a , b a,b を結ぶパスは、 c = l c a ( a , b ) c=lca(a,b) として、 a a から c c までは木を遡上し、
    # c c から b b まで下ることとなる。 根から各頂点への距離 d i s t [ v ] depth[v] を記録しておけば、
    # 簡単な計算で2点間距離を求めることができる。
    # depth[a]+depth[b]−2depth[c] 「 a a から根まで遡上し、根から b b まで下る、という経路の内、根～ c c の往復分が無駄である」と考えるとよい。
    if (lca.depth[c - 1] + lca.depth[d - 1] - 2 * lca.depth[common]) % 2 == 0:
        print("Town")
    else:
        print("Road")
