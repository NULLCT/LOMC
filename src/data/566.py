from collections import deque

N, Q = map(int, input().split())
g = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
#幅優先探索
color = [-1 for i in range(N)]
color[0] = 0
q = deque([])
q.append(0)
while q:
    e = q.pop()
    for i in g[e]:
        if color[i] == -1:
            color[i] = 1 - color[e]
            q.append(i)
#print(color)
for i in range(Q):
    c, d = map(int, input().split())
    print("Road") if color[c - 1] != color[d - 1] else print("Town")
