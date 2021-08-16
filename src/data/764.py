import sys, collections

sys.setrecursionlimit(10**6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()
nsa = lambda: list(map(str, stdin.readline().split()))
ntp = lambda: tuple(map(int, stdin.readline().split()))
mod = 10**9 + 7
inf = 10**18

n, q = na()
to = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = na()
    a, b = a - 1, b - 1
    to[a].append(b)
    to[b].append(a)


#! LCAと距離
def EulerTour(to, root=0):
    n = len(to)
    depth = [-1] * n
    depth[root] = 0
    first_visit_index = [-1] * n
    res = []
    stack = collections.deque()
    stack.append((root, 0))
    while stack:
        u, i = stack.pop()
        if i == 0: first_visit_index[u] = len(res)
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
        if Lmin < Rmin: Rmin = Lmin
        return Rmin


et, fi, dep = EulerTour(to)
sp = SparseTableMin([dep[u] for u in et])

for _ in range(q):
    c, d = na()
    c, d = c - 1, d - 1
    A = dep[c] + dep[d] - 2 * dep[sp.min(c, d)]
    if A % 2 == 0:
        print('Town')
    else:
        print('Road')
