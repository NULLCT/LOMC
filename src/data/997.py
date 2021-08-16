class LCA:
    """
    オイラーツアーとRMQでLCAを求める
    n: 木の頂点数
    edge: 辺のリストのリスト
    root: 根（デフォルト0）

    計算量
    初期化: O(N)
    クエリ: O(logN)
    定数倍が重い
    """
    class SegmentTree:
        def __init__(self, op, e, n, array=None):
            self.e = e
            self.op = op
            self.n = n
            self.log = (self.n - 1).bit_length()
            self.size = 1 << self.log
            self.d = [e] * (2 * self.size)

            if array:
                for i in range(self.n):
                    self.d[self.size + i] = array[i]
                for i in reversed(range(1, self.size)):
                    self.__update(i)

        def set(self, p, x):
            """
            a[p] に x を代入する
            """
            p += self.size
            self.d[p] = x
            for i in range(1, self.log + 1):
                self.__update(p >> i)

        def get(self, p):
            """
            a[p]を返す
            """
            return self.d[p + self.size]

        def prod(self, l, r):
            """
            [l, r) の総積を返す
            """
            op = self.op

            sml = self.e
            smr = self.e

            l += self.size
            r += self.size

            while l < r:
                if l & 1:
                    sml = op(sml, self.d[l])
                    l += 1
                if r & 1:
                    r -= 1
                    smr = op(self.d[r], smr)
                l >>= 1
                r >>= 1
            return op(sml, smr)

        def all_prod(self):
            """
            [0, n) の総積を返す
            """
            return self.d[1]

        def max_right(self, l, f):
            if l == self.n:
                return self.n
            op = self.op
            size = self.size
            l += size
            sm = self.e

            while True:
                while not (l & 1):
                    l >>= 1
                if not f(op(sm, self.d[l])):
                    while l < size:
                        l <<= 1
                        if f(op(sm, self.d[l])):
                            sm = op(sm, self.d[l])
                            l += 1
                    return l - size
                sm = op(sm, self.d[l])
                l += 1
                if (l & -l) == l:
                    break
            return self.n

        def min_left(self, r, f):
            if r == 0:
                return 0
            op = self.op
            size = self.size
            r += self.size
            sm = self.e

            while True:
                r -= 1
                while r and r & 1:
                    r >>= 1
                if not f(op(self.d[r], sm)):
                    while r < size:
                        r = 2 * r + 1
                        if f(op(self.d[r], sm)):
                            sm = op(self.d[r], sm)
                            r -= 1
                    return r + 1 - size
                sm = op(self.d[r], sm)
                if (r & -r) == r:
                    break
            return 0

        def __update(self, k):
            self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def __init__(self, n, edge, root=0):
        self.n = n
        self.root = root
        self.edge = edge
        self.et = []
        self.id = [-1] * self.n
        self.depth = []
        self._init_euler_tour()
        self.depth.append(float("inf"))  # indexを取得するRMQの単位元用

        def f(x, y):
            return x if self.depth[x] < self.depth[y] else y

        self.seg = self.SegmentTree(f, 2 * n - 1, 2 * n,
                                    [i for i in range(2 * n)])

    def _init_euler_tour(self):
        seen = [False] * self.n
        stack_v = [self.root]
        stack_d = [0]

        while stack_v:
            u = stack_v.pop()
            d = stack_d.pop()
            if u >= 0:
                seen[u] = True
                self.et.append(u)
                self.depth.append(d)

                for v in self.edge[u][::-1]:
                    if seen[v]:
                        continue
                    stack_v.append(~u)
                    stack_v.append(v)
                    stack_d.append(d)
                    stack_d.append(d + 1)
            else:
                self.et.append(~u)
                self.depth.append(d)

        for i, u in enumerate(self.et):
            if self.id[u] == -1:
                self.id[u] = i

    def get_lca(self, u, v):
        x, y = min(self.id[u], self.id[v]), max(self.id[u], self.id[v])
        return self.et[self.seg.prod(x, y + 1)]


def main():
    import sys
    read = sys.stdin.read
    readline = sys.stdin.readline
    INF = float('INF')
    # INF = (1 << 62) - (1 << 31)
    MOD = 10**9 + 7
    sys.setrecursionlimit(10**5)
    N, Q = map(int, readline().split())
    edge = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = (x - 1 for x in map(int, readline().split()))
        edge[a].append(b)
        edge[b].append(a)

    lca = LCA(N, edge)

    for _ in range(Q):
        c, d = (x - 1 for x in map(int, readline().split()))
        p = lca.get_lca(c, d)
        dist = lca.id[c] + lca.id[d] - 2 * lca.id[p]
        print('Town' if dist % 2 == 0 else 'Road')


if __name__ == '__main__':
    main()
