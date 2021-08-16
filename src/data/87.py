from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

visited = [-1] * n
temp = deque([0])
visited[0] = 0

while temp:
    p = temp.popleft()
    for pp in g[p]:
        if visited[pp] != -1: continue
        visited[pp] = visited[p] + 1
        temp.append(pp)

for i in range(q):
    c, d = map(int, input().split())
    if visited[c - 1] % 2 == visited[d - 1] % 2: print('Town')
    else: print('Road')
