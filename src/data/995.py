import sys

sys.setrecursionlimit(
    700000)  # if you think this value, change pypy to python3...?


def s_in():
    return input()


def n_in():
    return int(input())


def l_in():
    return list(map(int, input().split()))


class LCA:
    def __init__(self, n, root, edges):
        self.n = n
        self.depth, parents = tree_depth(n, root, edges)
        k = n.bit_length()
        self.double = Doubling(n, k, parents)

    def get_lca(self, u, v):
        dd = self.depth[v] - self.depth[u]
        if dd < 0:
            u, v = v, u
            dd = -dd

        # assert depth[u] <= depth[v]
        for k in range(self.double.max_k + 1):
            if dd & 1:
                v = self.double.double[v][k]
            dd >>= 1

        # assert depth[u] == depth[v]
        if u == v:
            return u

        for k in range(self.double.max_k - 1, -1, -1):
            pu = self.double.double[u][k]
            pv = self.double.double[v][k]
            if pu != pv:
                u = pu
                v = pv

        # assert kprv[0][u] == kprv[0][v]
        return self.double.double[u][0]


def tree_depth(n, root, edges):
    depth = [-1] * n
    parents = [-1] * n
    depth[root] = 0
    parents[root] = root

    stack = [root]

    while len(stack) > 0:
        u = stack.pop()
        for v in edges[u]:
            if not depth[v] == -1: continue
            stack.append(v)
            parents[v] = u
            depth[v] = depth[u] + 1

    return depth, parents


class Doubling:
    def __init__(self, n, k, trans):
        self.n = n
        self.max_k = k
        double = [[-1] * k for _ in range(n)]

        for i in range(n):
            double[i][0] = trans[i]
        for j in range(1, k):
            for i in range(n):
                double[i][j] = double[double[i][j - 1]][j - 1]
        self.double = double

    def forward(self, p, step):
        while step > 0:
            for k in range(0, self.max_k):
                if 2**(k + 1) > step: break
            step -= 2**k
            p = self.double[p][k]
        return p


def _main(n, edges, q):
    lca = LCA(n, 1, edges)
    for c, d in q:
        u = lca.get_lca(c, d)
        d = (lca.depth[c] - lca.depth[u]) + (lca.depth[d] - lca.depth[u])

        if d % 2 == 0:
            print("Town")
        else:
            print("Road")


def main():
    n, qq = l_in()

    edges = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = l_in()
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    q = [None] * qq

    for i in range(qq):
        a, b = l_in()
        q[i] = (a - 1, b - 1)

    _main(n, edges, q)


if __name__ == "__main__":
    main()
