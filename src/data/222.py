N, Q = map(int, input().split())
roads_and_towns = [tuple(map(int, input().split())) for _ in range(N - 1)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

adj_list = [[] for _ in range(N)]
for u, v in roads_and_towns:
    adj_list[u - 1].append(v - 1)
    adj_list[v - 1].append(u - 1)

colors = [-1 for _ in range(N)]

from collections import deque

bfs = deque([0])
colors[0] = 0
while bfs:
    cur = bfs.popleft()

    for nbr in adj_list[cur]:
        if colors[nbr] == -1:
            colors[nbr] = 1 - colors[cur]
            bfs.append(nbr)

for u, v in queries:
    if colors[u - 1] == colors[v - 1]:
        print("Town")
    else:
        print("Road")
