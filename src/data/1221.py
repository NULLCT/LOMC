import sys

# sys.setrecursionlimit(200005)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def LI1():
    return list(map(int1, sys.stdin.readline().split()))


def LLI1(rows_number):
    return [LI1() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline().rstrip()


inf = 10**16
md = 10**9 + 7
# md = 998244353


class LCA:
    # 頂点は0～n-1
    def __init__(self, to, root=0):
        self.to = to
        self.n = len(to)
        self.parents = [-1] * (self.n + 1)
        self.depth = [0] * self.n
        self.__dfs(root)
        self.max_level = max(self.depth).bit_length()
        self.ancestor = [self.parents] + [[-1] * (self.n + 1)
                                          for _ in range(self.max_level)]
        row0 = self.ancestor[0]
        for lv in range(self.max_level):
            row1 = self.ancestor[lv + 1]
            for u in range(self.n):
                row1[u] = row0[row0[u]]
            row0 = row1

    def __dfs(self, root):
        stack = [root]
        while stack:
            u = stack.pop()
            pu = self.parents[u]
            du = self.depth[u]
            for v in self.to[u]:
                if v == pu: continue
                self.parents[v] = u
                self.depth[v] = du + 1
                stack.append(v)

    # 最小共通祖先
    def anc(self, u, v):
        diff = self.depth[u] - self.depth[v]
        if diff < 0: u, v = v, u
        diff = abs(diff)
        lv = 0
        while diff:
            if diff & 1: u = self.ancestor[lv][u]
            lv, diff = lv + 1, diff >> 1
        if u == v: return u
        for lv in range(self.depth[u].bit_length() - 1, -1, -1):
            anclv = self.ancestor[lv]
            if anclv[u] != anclv[v]: u, v = anclv[u], anclv[v]
        return self.parents[u]

    def dist(self, u, v):
        w = self.anc(u, v)
        return self.depth[u] + self.depth[v] - self.depth[w] * 2


n, q = LI()
to = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = LI1()
    to[u].append(v)
    to[v].append(u)

lca = LCA(to)
for _ in range(q):
    c, d = LI1()
    cur = lca.dist(c, d)
    print("Road" if cur & 1 else "Town")
