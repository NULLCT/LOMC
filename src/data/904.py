# author:  Taichicchi
# created: 10.07.2021 21:13:51

import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)


def EulerTour(to, root=0):
    n = len(to)
    depth = [-1] * n
    depth[root] = 0
    first_visit_index = [-1] * n
    res = []
    stack = [(root, 0)]
    while stack:
        u, i = stack.pop()
        if i == 0:
            first_visit_index[u] = len(res)
        res.append(u)
        if i < len(to[u]):
            v = to[u][i]
            stack.append((u, i + 1))
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                stack.append((v, 0))
            else:
                res.pop()
    return res, first_visit_index, depth


class SparseTableMin:
    def __init__(self, aa):
        w = len(aa)
        h = w.bit_length()
        table = [aa] + [[-1] * w for _ in range(h - 1)]
        tablei1 = table[0]
        for i in range(1, h):
            tablei = table[i]
            for j in range(w - (1 << i) + 1):
                rj = j + (1 << (i - 1))
                tablei[j] = min(tablei1[j], tablei1[rj])
            tablei1 = tablei
        self.table = table

    # [l,r)の最小値
    def min(self, l, r):
        i = (r - l).bit_length() - 1
        tablei = self.table[i]
        Lmin = tablei[l]
        Rmin = tablei[r - (1 << i)]
        if Lmin < Rmin:
            Rmin = Lmin
        return Rmin


# intにしてから1引く関数。頂点の入力に使う
def int1(x):
    return int(x) - 1


# et...オイラーツアーの頂点順
# fi...頂点がオイラーツアーで最初に現れるindex
# dep...頂点の深さ
et, fi, dep = EulerTour(G)
# オイラーツアーに対応させた深さのリストをスパーステーブルに渡す
sp = SparseTableMin([dep[u] for u in et])

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    q = sp.min(c, d)
    dist = 1 + dep[c] + dep[d] - 2 * dep[q]
    print("Town" if dist % 2 == 1 else "Road")
