import sys

input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10**6)


class Tree:
    def __init__(self, N):
        self.V = N
        self.edge = [[] for _ in range(N)]
        self.order = []

    def add_edges(self, ind=1, bi=True):
        for i in range(self.V - 1):
            a, b = map(int, input().split())
            a -= ind
            b -= ind
            self.edge[a].append(b)
            if bi: self.edge[b].append(a)

    def add_edge(self, a, b, bi=True):
        self.edge[a].append(b)
        if bi: self.edge[b].append(a)

    def dp(self, start):
        stack = deque([start])
        self.parent = [self.V] * self.V
        self.parent[start] = -1
        self.order.append(start)
        #記録したい値の配列を定義
        self.dp = [0] * self.V
        while stack:
            v = stack.pop()
            for u in self.edge[v]:
                if u == self.parent[v]: continue
                self.parent[u] = v
                self.dp[u] = self.dp[v] ^ 1
                stack.append(u)

    def bfs(self, start):
        d = deque([start])
        self.min_cost = [-1] * self.V
        self.min_cost[start] = 0
        while len(d) > 0:
            v = d.popleft()
            for w in self.edge[v]:
                if self.min_cost[w] == -1:
                    self.min_cost[w] = self.min_cost[v] + 1
                    d.append(w)
        return


N, Q = map(int, input().split())
G = Tree(N)
G.add_edges(ind=1, bi=True)
G.dp(0)
ans = ['Road'] * Q
for i in range(Q):
    c, d = map(int, input().split())
    if G.dp[c - 1] == G.dp[d - 1]: ans[i] = 'Town'
print(*ans, sep='\n')
