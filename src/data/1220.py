#!/usr/bin python3
# -*- coding: utf-8 -*-


class Tree():
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.root = None  # 根
        self.etnodes = []  # i番目の頂点番号
        self.etedges = []  # i番目の辺の番号
        self.etL = [0] * n  # in
        self.etR = [0] * n  # out
        self.depthbynodes = [0] * n
        self.etdepth = []  # i番目の辺の

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def set_euler_tour(self, root):
        self.root = root  # 根を設定して
        pa = [0] * self.n
        stack = [~root, root]
        ct = -1
        de = -1
        while stack:
            v = stack.pop()
            ct += 1
            self.etedges.append(v)
            if v >= 0:
                de += 1
                self.etnodes.append(v)
                self.etdepth.append(de)
                self.etL[v] = ct
                self.depthbynodes[v] = de
                p = pa[v]
                for w in self.edges[v][::-1]:
                    if w == p: continue
                    pa[w] = v
                    stack.append(~w)
                    stack.append(w)
            else:
                de -= 1
                if de < 0:
                    self.etdepth.append(self.n)
                else:
                    self.etdepth.append(de)
                self.etnodes.append(pa[~v])
                self.etR[~v] = ct


#############################################
class SegmentTree:
    # 初期化処理
    # f     : SegmentTreeにのせるモノイド
    # idele : fに対する単位元
    def __init__(self, size, f=lambda x, y: min(x, y), idele=float('inf')):
        self.size = 2**(size - 1).bit_length()  # 簡単のため要素数nを2冪にする
        self.idele = idele  # 単位元
        self.f = f  # モノイド
        self.dat = [(self.idele, -1)] * (self.size * 2)  # 要素を単位元で初期化

## one point

    def update(self, i, x):
        i += self.size  # 1番下の層におけるインデックス
        self.dat[i] = (x, i)
        while i > 0:  # 層をのぼりながら値を更新 indexが0になれば終了
            i >>= 1  # 1つ上の層のインデックス(完全二分木における親)
            # 下の層2つの演算結果の代入(完全二分木における子同士の演算)
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])

## range

    def query(self, l, r):
        l += self.size  # 1番下の層におけるインデックス
        r += self.size  # 1番下の層におけるインデックス
        lres, rres = (self.idele, -1), (self.idele, -1)  # 左側の答えと右側の答えを初期化
        while l < r:  # lとrが重なるまで上記の判定を用いて演算を実行
            # 左が子同士の右側(lが奇数)(lの末桁=1)ならば、dat[l]を加算
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1
            # 右が子同士の右側(rが奇数)(rの末桁=1)ならば、dat[r-1]を加算
            if r & 1:
                r -= 1
                rres = self.f(self.dat[r],
                              rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

    def init(self, a):
        for i, x in enumerate(a):
            # 1番下の層におけるインデックス
            self.dat[i + self.size] = (x, i)
        for i in range(self.size - 1, -1, -1):
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])


############################################
n, q = map(int, input().split())
T = Tree(n)
for _ in range(n - 1):
    a, b = map(int, input().split())
    T.add_edge(a - 1, b - 1)

T.set_euler_tour(0)
depth = T.etdepth

SGT = SegmentTree(len(depth))
SGT.init(depth)

for i in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l = T.etL[a]
    r = T.etL[b]
    if l > r:
        l, r = r, l
    r += 1
    x = SGT.query(l, r)[1]
    lca = T.etnodes[x]
    d = T.depthbynodes[a] + T.depthbynodes[b] - 2 * T.depthbynodes[lca]
    if d % 2 == 0:
        print('Town')
    else:
        print('Road')
