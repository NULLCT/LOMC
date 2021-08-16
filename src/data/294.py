import heapq

N, Q = map(int, input().split())
INF = float('inf')
G = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append([1, b - 1])
    G[b - 1].append([1, a - 1])


def dijkstra(N, start, goal, edge_list):
    Q = []
    #始点距離＝0, (dist, vertex)
    heapq.heappush(Q, (0, start))
    dist = [-1] * N
    dist[start] = 0
    while len(Q) > 0:
        d, v = heapq.heappop(Q)
        for nd, nv in edge_list[v]:
            if dist[nv] == -1 or dist[nv] > d + nd:
                dist[nv] = d + nd
                heapq.heappush(Q, (dist[nv], nv))

    return dist


cost = dijkstra(N, 0, N, G)

for i in range(Q):
    c, d = map(int, input().split())
    cost_c = cost[c - 1]
    cost_d = cost[d - 1]

    if abs(cost_c - cost_d) % 2 == 0:
        print('Town')
    else:
        print('Road')
