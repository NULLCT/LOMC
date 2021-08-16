from collections import deque

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

seen = [False] * n
cnt = [0] * n
que = deque([0])
pre = 0

while que:
    v = que.popleft()
    seen[v] = True
    for u in graph[v]:
        if seen[u] == True: continue
        que.append(u)
        cnt[u] = cnt[v] ^ 1

for _ in range(q):
    c, d = map(int, input().split())
    if cnt[c - 1] != cnt[d - 1]:
        print("Road")
    else:
        print("Town")
