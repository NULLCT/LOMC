import sys

MAXX = 10**6 + 1
sys.setrecursionlimit(MAXX)
input = sys.stdin.readline


class SegTree:  #1-indexセグ木
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: default値
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


N, Q = map(int, input().split())
adj = [[] for _ in range(N + 2)]
for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

label = []
lvl = []
id = [0] * (N + 2)
count = 0


def dfs(v, parent, depth):
    global count
    count += 1
    label.append(v)
    lvl.append(depth)
    if id[v] <= 0:
        id[v] = count
    for u in adj[v]:
        if u == parent: continue
        dfs(u, v, depth + 1)
        count += 1
        label.append(v)
        lvl.append(depth)


dfs(1, 0, 0)
# #lcaを計算するため、訪れる順のstackをセグメント木に入れる
# treeid = []
# for v in label:
#     treeid.append(id[v]) #ノードIDから訪れる順に変換して格納
# tree = SegTree(treeid, min, MAXX)
#print(treeid)
for _ in range(Q):
    u, v = map(int, input().split())
    ll, rr = id[u] - 1, id[v] - 1  #ノードIDから訪れる順に変換
    # if ll > rr: ll, rr = rr, ll
    # lca_id = tree.query(ll, rr+1) #その区間の最小値がLCA
    # lca = label[lca_id-1] #LCAノードのID
    dist = lvl[ll] + lvl[rr]  #- 2*lvl[id[lca]-1]
    #print(u, v, lca, dist)
    if dist & 0x01 == 0:
        print('Town')
    else:
        print('Road')
