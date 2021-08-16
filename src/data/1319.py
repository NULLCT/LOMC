import sys
from collections import deque

sys.setrecursionlimit(10**7)


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI2():
    return list(map(int, sys.stdin.readline().rstrip()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def LS2():
    return list(sys.stdin.readline().rstrip())


class LCA():
    def __init__(self, N, Graph, root):
        '''
        N:頂点数,Graph:木の隣接リスト表現,root:根 (0-index)
        '''
        self.N = N
        self.par = [-1] * N
        self.depth = [-1] * N

        deq = deque([root])
        self.depth[root] = 0
        while deq:
            u = deq.pop()
            for v in Graph[u]:
                if self.depth[v] != -1:
                    continue
                self.par[v] = u
                self.depth[v] = self.depth[u] + 1
                deq.appendleft(v)

        self.ancestor = [self.par]
        self.K = (N - 1).bit_length() + 1
        for _ in range(self.K - 1):
            new = [0] * N
            for u in range(N):
                if self.ancestor[-1][u] == -1:
                    new[u] = -1
                else:
                    new[u] = self.ancestor[-1][self.ancestor[-1][u]]
            self.ancestor.append(new)

    def lca(self, u, v):
        depth_diff = self.depth[u] - self.depth[v]
        if depth_diff < 0:
            u, v = v, u
            depth_diff *= -1
        # depth[u] >= depth[v] としてよい

        for k in range(self.K):
            if depth_diff & 1:
                u = self.ancestor[k][u]
            depth_diff >>= 1
        # depth[u] == depth[v] としてよい

        if u == v:
            return u
        for k in range(self.K - 1, -1, -1):
            pu, pv = self.ancestor[k][u], self.ancestor[k][v]
            if pu != pv:
                u, v = pu, pv
        return self.ancestor[0][u]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]


N, Q = MI()
Graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = MI()
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

lca = LCA(N, Graph, 0)
for _ in range(Q):
    c, d = MI()
    c -= 1
    d -= 1
    di = lca.dist(c, d)
    if di % 2 == 0:
        print('Town')
    else:
        print('Road')
