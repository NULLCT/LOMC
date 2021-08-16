from collections import deque, defaultdict


class Bfs:
    def __init__(self, graph):
        self.cache = dict()
        self.graph = graph

    def bfs(self, c: int, d: int):
        self.cache[(c, c)] = 0
        self.cache[(d, d)] = 0
        q = deque()
        q.append(c)
        searched = set()
        while q:
            v = q.popleft()
            searched.add(v)
            for n in self.graph[v]:
                if n not in searched:
                    self.cache[(c, n)] = self.cache[(c, v)] + 1
                    self.cache[(n, c)] = self.cache[(c, n)]
                    q.append(n)
        return self.cache

    def find(self, c: int, d: int, first):
        return abs(self.cache[(first, d)] - self.cache[(first, c)])


def main() -> int:
    N, Q = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs = Bfs(graph)
    flag = True
    for _ in range(Q):
        c, d = map(int, input().split())
        if flag:
            bfs.bfs(c, d)
            first = c
            flag = False
        ret = bfs.find(c, d, first)
        # print(ret)
        # continue
        if ret % 2 == 1:
            print('Road')
        else:
            print('Town')


main()
