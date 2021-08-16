import sys


def segfunc(x, y):
    return x + y


ide_ele = 0


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] += x
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

    def get(self, k):
        return self.query(k, k + 1)


N, Q = map(int, input().split())
path = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)

S = []
F = [0] * N

sys.setrecursionlimit(10**6)

q = [0]
INF = 10**18

depth = [INF] * N
depth[0] = 0

while q:
    at = q.pop()
    for to in path[at]:
        if depth[to] != INF:
            continue
        q.append(to)
        depth[to] = depth[at] + 1


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in path[v]:
        dfs(w, d + 1)
        S.append(v)


for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (depth[c] + depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
