from collections import deque

n, q = map(int, input().split())
colors = [None] * n
e_list = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    e_list[a - 1].append(b - 1)
    e_list[b - 1].append(a - 1)
waiting = deque()
waiting.append(0)
colors[0] = 1
while waiting:
    u = waiting.popleft()
    for v in e_list[u]:
        if not colors[v]:
            colors[v] = 3 - colors[u]
            waiting.append(v)
for _ in range(q):
    c, d = map(int, input().split())
    if colors[c - 1] == colors[d - 1]:
        print("Town")
    else:
        print("Road")
