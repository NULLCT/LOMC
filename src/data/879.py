from sys import stdin

input = stdin.readline
from collections import deque

N, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
level = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [False] * (N + 1)


def bfs(st):
    global level
    q = deque()
    q.append([st, 0])
    visited[st] = True
    while q:
        for _ in range(len(q)):
            now, lvl = q.popleft()
            for next in tree[now]:
                if not visited[next]:
                    q.append([next, lvl + 1])
                    level[next] = lvl + 1
                    visited[next] = True


bfs(1)


def solve(a, b):
    if abs(level[a] - level[b]) % 2 == 1:
        return 'Road'
    else:
        return 'Town'


for _ in range(Q):
    x, y = map(int, input().split())
    print(solve(x, y))
