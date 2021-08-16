from collections import deque


class Reunion:
    def __init__(self, N):
        self.depthmap = [-1 for i in range(N + 1)]
        self.graph = [[] for _ in range(N + 1)]

    def adding(self, a, b):
        self.graph[b].append(a)
        self.graph[a].append(b)

    def valid(self):
        queue = deque()
        queue.append((1, 0))
        while len(queue) > 0:
            (node, depth) = queue.pop()
            self.depthmap[node] = depth
            for child in self.graph[node]:
                if self.depthmap[child] >= 0:
                    continue
                queue.append((child, depth + 1))

    def judge(self, a, b):
        if (self.depthmap[a] + self.depthmap[b]) % 2 == 0:
            print('Town')
        else:
            print('Road')


N, q = map(int, input().split())
RU = Reunion(N)
for _ in range(N - 1):
    a, b = map(int, input().split())
    RU.adding(a, b)
RU.valid()
for _ in range(q):
    a, b = map(int, input().split())
    RU.judge(a, b)
