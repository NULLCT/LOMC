N, K = map(int, input().split())

L = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)


class LCA_doubling:
    """
    parent: ダブリングテーブル
    depth: 元の深さ
    """
    def __init__(self, g, root):  #g: graph
        def dfs(root):
            n = len(g)
            parent = self.parent[0]
            q = [root]
            while q:
                v = q.pop()
                for c in g[v]:
                    if c != parent[v]:
                        self.depth[c] = self.depth[v] + 1
                        parent[c] = v
                        q.append(c)

        def doubling_make_table(N, logN, Table):
            for i in range(1, logN):
                for j, Tiij in enumerate(Table[i - 1]):
                    if Tiij != -1:
                        Table[i][j] = Table[i - 1][Tiij]

        N = len(g)
        self.logN = len(bin(N))
        self.parent = [[-1] * N for _ in range(self.logN)]
        self.depth = [0] * (N)  #ノードの深さ
        dfs(root)  #root を根とする木と見て計算
        doubling_make_table(N, self.logN, self.parent)  #ダブリングのテープル構築

    def getLCA(self, u, v):  #u,vのLCAを返す
        if self.depth[u] > self.depth[v]: u, v = v, u  #vが深い
        dd = self.depth[v] - self.depth[u]
        for k in range(self.logN - 1, -1, -1):
            if (dd >> k) & 1: v = self.parent[k][v]
        if u == v: return u
        for k in range(self.logN - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u, v = self.parent[k][u], self.parent[k][v]
        return self.parent[0][u]

    def getdepth(self, u):  #uの深さを返す
        return self.depth[u]


root = 1
LCA = LCA_doubling(L, root)
#print(LCA.parent)
#print(LCA.depth[1])
for k in range(K):
    a, b = map(int, input().split())
    B = LCA.getLCA(a, b)
    #print(B)
    cnt = LCA.depth[a] - (LCA.depth[B]) + LCA.depth[b] - (LCA.depth[B])
    if cnt % 2 == 1:
        print("Road")
    else:
        print("Town")
