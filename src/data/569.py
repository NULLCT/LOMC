from collections import deque

n, q = map(int, input().split())
G = [[] for i in range(n)]

for i in range(n - 1):
    ind = lambda n: int(n) - 1
    a, b = map(ind, input().split())
    G[a].append(b)
    G[b].append(a)

que = deque()
color = [-1 for _ in range(n)]
color[0] = 0
que.append(0)

while len(que) > 0:
    t = que.pop()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.append(i)

for i in range(q):
    ind = lambda n: int(n) - 1
    a, b = map(ind, input().split())
    print('Town' if color[a] == color[b] else 'Road')
