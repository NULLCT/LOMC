class SegTree:
    def __init__(self, init_val, ide_ele, segfunc):
        self.n = len(init_val)
        self.num = 2**(self.n - 1).bit_length()
        self.ide_ele = ide_ele
        self.segfunc = segfunc
        self.seg = [ide_ele] * 2 * self.num
        # set_val
        for i in range(self.n):
            self.seg[i + self.num] = init_val[i]
        # built
        for i in range(self.num - 1, 0, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.seg[k] = x
        while k:
            k = k >> 1
            self.seg[k] = self.segfunc(self.seg[2 * k], self.seg[2 * k + 1])

    def query(self, l, r):
        if r <= l:
            return self.ide_ele
        l += self.num
        r += self.num
        res = self.ide_ele
        while l < r:
            if r & 1:
                r -= 1
                res = self.segfunc(res, self.seg[r])
            if l & 1:
                res = self.segfunc(res, self.seg[l])
                l += 1
            l = l >> 1
            r = r >> 1
        return res


def segfunc(x, y):
    if x <= y:
        return x
    else:
        return y


ide_ele = 10**18


class LCA:
    def __init__(self, g, root):
        # g: adjacency list
        # root
        self.n = len(g)
        self.root = root

        s = [self.root]
        self.parent = [-1] * self.n
        self.child = [[] for _ in range(self.n)]
        visit = [-1] * self.n
        visit[self.root] = 0
        while s:
            v = s.pop()
            for u in g[v]:
                if visit[u] == -1:
                    self.parent[u] = v
                    self.child[v].append(u)
                    visit[u] = 0
                    s.append(u)

        # Euler tour
        tank = [self.root]
        self.eulerTour = []
        self.left = [0] * self.n
        self.right = [-1] * self.n
        self.depth = [-1] * self.n

        eulerNum = -1
        de = -1

        while tank:
            v = tank.pop()
            if v >= 0:
                eulerNum += 1
                self.eulerTour.append(v)
                self.left[v] = eulerNum
                self.right[v] = eulerNum
                tank.append(~v)
                de += 1
                self.depth[v] = de
                for u in self.child[v]:
                    tank.append(u)
            else:
                de -= 1
                if ~v != self.root:
                    self.eulerTour.append(self.parent[~v])
                    eulerNum += 1
                    self.right[self.parent[~v]] = eulerNum

        #A = [self.depth[e] for e in self.eulerTour]
        A = [0] * (2 * self.n - 1)
        for i, e in enumerate(self.eulerTour):
            A[i] = self.depth[e] * (2 * self.n - 1) + i
        self.seg = SegTree(A, ide_ele, segfunc)

    def getLCA(self, u, v):
        # u, v: 0-indexed
        p = min(self.left[u], self.left[v])
        q = max(self.right[u], self.left[v]) + 1
        m = self.seg.query(p, q)
        return self.eulerTour[m % (2 * self.n - 1)]


import sys
import io, os
#input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

lca = LCA(g, 0)


def dist(u, v):
    l = lca.getLCA(u, v)
    res = lca.depth[u] + lca.depth[v] - 2 * lca.depth[l]
    return res


for j in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    x = dist(c, d)
    if x % 2 == 1:
        print('Road')
    else:
        print('Town')
