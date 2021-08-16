class WeightedUnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        # 親ノードとの重み
        self.diff_weight = [0 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        # 親ノードはまだ上書きしない
        root = self.find(self.par[x])
        self.diff_weight[x] += self.diff_weight[self.par[x]]
        self.par[x] = root
        return self.par[x]

    def weight(self, x):
        """ x 根に対する重みを返す """
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        """ x と y の差分をとる """
        return self.weight(y) - self.weight(x)

    def unite(self, x, y, w):
        """ ノード x の下にノード y をつける。辺の重みは、w """
        # ただし、実際には、x の根と y の 根をくっつけるので、補正
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            # y の下に x をつけることになるので、重さは反転させる
            self.par[x] = y
            w = -w
            self.diff_weight[x] = w
        elif self.rank[y] < self.rank[x]:
            self.par[y] = x
            self.diff_weight[y] = w
        else:
            self.par[y] = x
            self.rank[x] += 1
            self.diff_weight[y] = w


N, Q = map(int, input().split())
uf = WeightedUnionFind(N)
for i in range(N - 1):
    a, b = map(int, input().split())  #a,b:つながっている辺
    uf.unite(a - 1, b - 1, 1)

for i in range(Q):
    c, d = map(int, input().split())  #a,b:つながっている辺
    if uf.diff(c - 1, d - 1) % 2 == 0:
        print("Town")
    else:
        print("Road")
