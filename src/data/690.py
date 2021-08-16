from collections import deque


def BFS(start):
    dist = [-1] * N
    dist[start] = 0
    que = deque([start])
    while que:
        fr = que.popleft()
        for to in edge[fr]:
            if dist[to] == -1:
                dist[to] = dist[fr] + 1
                que.append(to)

    return dist


N, Q = map(int, input().split())
N_list = list(range(N))
edge = [[] for _ in N_list]
for i in [0] * (N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
arr = BFS(0)
ma = [''] * N
for i in range(N):
    if arr[i] % 2 == 0:
        ma[i] = 'R'
    else:
        ma[i] = 'B'

for i in range(Q):
    c, d = map(int, input().split())
    if ma[c - 1] == ma[d - 1]:
        print("Town")
    else:
        print("Road")
