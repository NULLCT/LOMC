from collections import deque
import sys

read = sys.stdin.readline

n, q = map(int, read().split())
path = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, read().split())
    a, b = a - 1, b - 1
    path[a].append(b)
    path[b].append(a)

flag = [-1] * n
flag[0] = 0
que = deque([[0, 0]])
while que:
    x, c = que.popleft()
    for y in path[x]:
        if flag[y] >= 0:
            continue
        flag[y] = (c + 1) % 2
        que.append([y, c + 1])

for _ in range(q):
    s, t = map(int, read().split())
    s, t = s - 1, t - 1
    print('Road' if flag[s] ^ flag[t] else 'Town')
