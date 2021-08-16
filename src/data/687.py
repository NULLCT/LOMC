import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def I():
    return int(input())


def LI():
    return list(map(int, input().split()))


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def S():
    return input()


def LS():
    return input().split()


INF = float('inf')


class Graph:
    def __init__(self, n, is_directed=False):
        """
        :param n: 頂点数
        :param is_directed: 有向グラフ(True)か無向グラフか(False)
        """
        self.graph = [[] for _ in range(n)]
        self.is_directed = is_directed

    def add_edge(self, u, v):
        """頂点uから頂点vに辺を作る
        無向グラフの場合、uからvの方向の辺のみを記録する
        """
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def bfs(self, start):
        """幅優先探索を行い始点から各頂点までの距離の配列を返す
        """
        distances = [INF] * len(self.graph)
        queue = deque([start])
        distances[start] = 0
        # ans = [0] * len(self.graph)

        while queue:
            now = queue.popleft()
            for to in self.graph[now]:
                if distances[to] != INF:
                    continue
                queue.append(to)
                distances[to] = distances[now] + 1
        return distances

    def dfs(self, start):
        """深さ優先探索を行い始点から各頂点までの距離の配列を返す
        """
        distances = [INF] * len(self.graph)
        queue = deque([start])
        distances[start] = 0

        while queue:
            now = queue.pop()
            for to in self.graph[now]:
                if distances[to] != INF:
                    continue
                queue.append(to)
                # 前の頂点からこの頂点に対する道標を建てる
                distances[to] = distances[now] + 1
        return distances


n, q = LI()
g = Graph(n)
for _ in range(n - 1):
    a, b = LI()
    a -= 1
    b -= 1
    g.add_edge(a, b)

ques = []
for _ in range(q):
    c, d = LI()
    c -= 1
    d -= 1
    ques.append([c, d])

dist = g.dfs(0)

for (c, d) in ques:
    m = abs(dist[c] - dist[d]) % 2
    print('Road' if m == 1 else 'Town')
