n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


class LCA_doubling:
    def __init__(self, n, graph, start):
        self.n = n
        self.graph = graph
        self.start = start

        # graph and n is necessary
        def dfs(start):
            par = [-1] * n
            depth = [-1] * n
            euler = []
            stack = []
            stack.append(start)
            depth[start] = 0
            while stack:
                v = stack.pop()
                euler.append(v)
                d = depth[v]
                for u in graph[v]:
                    if par[v] == u:
                        continue
                    par[u] = v
                    depth[u] = d + 1
                    stack.append(u)
            return par, depth

        self.par, self.depth = dfs(self.start)
        self.num = self.n.bit_length() + 1
        self.doubling = [[-1] * (self.num) for _ in range(n)]

        for i in range(n):
            self.doubling[i][0] = self.par[i]

        for d in range(self.num - 1):
            nd = d + 1
            for i in range(n):
                if self.doubling[i][d] == -1:
                    self.doubling[i][nd] = -1
                else:
                    self.doubling[i][nd] = self.doubling[self.doubling[i]
                                                         [d]][d]

    def query(self, a, b):
        def soroeru(a, b):
            if self.depth[a] == self.depth[b]:
                return a, b
            elif self.depth[a] < self.depth[b]:
                a, b = b, a
            delta = self.depth[a] - self.depth[b]
            assert delta > 0
            now = a
            for i in range(self.num):
                if (delta >> i) & 1:
                    now = self.doubling[now][i]
            assert self.depth[now] == self.depth[b]
            return now, b

        a, b = soroeru(a, b)
        if a == b:
            return a
        for i in range(self.num)[::-1]:
            if self.doubling[a][i] != self.doubling[b][i]:
                a = self.doubling[a][i]
                b = self.doubling[b][i]
        return self.doubling[a][0]


LCA = LCA_doubling(n, graph, 0)
for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    cc = LCA.query(c, d)
    dist = LCA.depth[d] + LCA.depth[c] - 2 * LCA.depth[cc]
    if dist % 2:
        print("Road")
    else:
        print("Town")
