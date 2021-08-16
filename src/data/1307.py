from collections import deque


class LCA:
    "0-indexed"

    __slots__ = ["depth", "ancestor"]

    def __init__(self, adj):
        N = len(adj)
        parent = [-1] * N
        self.depth = [0] * N
        q = deque([0])
        while q:
            node = q.popleft()
            for next_node in adj[node]:
                if parent[node] != next_node:
                    parent[next_node] = node
                    q.append(next_node)
                    self.depth[next_node] = self.depth[node] + 1

        self.ancestor = [parent]  #self.ancestor[k][u]はuの2**k先の祖先。
        k = 1
        while (1 << k) < N:
            anc_k = [0] * N
            for u in range(N):
                if self.ancestor[-1][u] == -1:
                    anc_k[u] = -1
                else:
                    anc_k[u] = self.ancestor[-1][self.ancestor[-1][u]]
            self.ancestor.append(anc_k)
            k += 1

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for k, bit in enumerate(
                reversed(format(self.depth[u] - self.depth[v], 'b'))):
            if bit == '1':
                u = self.ancestor[k][u]
        if u == v:
            return u
        for anc in reversed(self.ancestor):
            if anc[u] != anc[v]:
                u = anc[u]
                v = anc[v]
        return self.ancestor[0][u]

    def dist(self, u, v):
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]


def main():
    import sys
    input = sys.stdin.buffer.readline

    N, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    lca = LCA(adj)
    for _ in range(Q):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        print("Road" if lca.dist(u, v) % 2 else "Town")


if __name__ == "__main__":
    main()
