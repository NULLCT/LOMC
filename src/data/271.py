N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N + 1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

INF = 10**18
dist = [INF] * (N + 1)

dist[1] = 0
stack = [1]

while stack:
    i = stack.pop()
    #print(i, dist)
    for j in graph[i]:
        if dist[j] == INF:
            dist[j] = dist[i] + 1
            stack.append(j)


def road_or_town(i, j):
    if (dist[i] + dist[j]) % 2:
        return "Road"
    else:
        return "Town"


for c, d in CD:
    print(road_or_town(c, d))
