from collections import deque

N, Q = map(int, input().split())
#G=: _番目の町に隣接している町リスト
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
que = deque()
color = [-1] * N
color[0] = 0
que.append(0)

while que:
    now = que.pop()
    for i in G[now]:
        if color[i] == -1:
            color[i] = color[now] + 1
            que.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    ans = "Town"
    if color[c - 1] % 2 != color[d - 1] % 2:
        ans = "Road"
    print(ans)
