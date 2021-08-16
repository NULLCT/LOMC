from collections import deque, Counter, defaultdict
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
E = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

INF = 10**18


class SegTree():
    def __init__(self, size, segfunc, ide_ele):
        self.size = 2**(size - 1).bit_length()
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.tree = [ide_ele] * (self.size * 2)

    def update(self, k, a):
        k += self.size
        self.tree[k] = a
        while k > 0:
            k >>= 1
            self.tree[k] = self.segfunc(self.tree[k * 2], self.tree[k * 2 + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.ide_ele, self.ide_ele
        while l < r:
            if (l & 1):
                lres = self.segfunc(lres, self.tree[l])
                l += 1
            if (r & 1):
                r -= 1
                rres = self.segfunc(self.tree[r], rres)
            l >>= 1
            r >>= 1
        res = self.segfunc(lres, rres)
        return res


# Euler Tour
def euler_tour(n, G, s):
    stack = deque([~s, s])
    done = [0] * n
    time = 0
    d = -1

    in_t = [0] * n  # in time
    out_t = [0] * n  # out time
    depth = [0] * n  # depth
    et = []  # euler tour 探索順
    p = [0] * n  # parent

    while stack:
        cur = stack.pop()
        # 行きがけ処理
        if cur >= 0:
            done[cur] = 1
            et.append(cur)
            in_t[cur] = time
            d += 1
            depth[cur] = d
            for e in G[cur]:
                if done[e]: continue
                stack.append(~e)
                stack.append(e)
                p[e] = cur
            time += 1
        # 帰りがけ処理
        else:
            out_t[~cur] = time
            et.append(p[~cur])
            d -= 1
            time += 1

    return et, in_t, out_t, depth


class LCA():
    def __init__(self, n, E, start):
        self.et, self.in_t, self.out_t, self.depth = euler_tour(n, E, start)
        self.seg = SegTree(len(self.et), lambda a, b: a
                           if a[0] <= b[0] else b, (INF, 0))
        for i, eti in enumerate(self.et):
            self.seg.update(i, (self.depth[eti], eti))

    def query(self, a, b):
        l, r = sorted([self.in_t[a], self.in_t[b]])
        depth_p, p = self.seg.query(l, r + 1)
        return depth_p, p


lca = LCA(n, E, 0)
for i in range(q):
    c, d = map(int, input().split())
    depth_c = lca.depth[c - 1]
    depth_d = lca.depth[d - 1]
    depth_p, p = lca.query(c - 1, d - 1)

    if (abs(depth_c - depth_p) - abs(depth_d - depth_p)) % 2:
        print("Road")
    else:
        print("Town")
