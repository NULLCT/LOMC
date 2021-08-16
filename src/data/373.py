from collections import deque

n, q = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
que = deque()
color = [-1 for i in range(n)]
color[0] = 0
que.append(0)
while not len(que) == 0:
    t = que.popleft()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.append(i)
for i in range(q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
