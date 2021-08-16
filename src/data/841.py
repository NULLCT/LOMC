import sys
import heapq

input = sys.stdin.readline


def dijkstra(V, e_list):
    inf = float('inf')
    done = [False] * V
    dist = [inf] * V
    dist[0] = 0
    node_heap = []
    heapq.heappush(node_heap, [dist[0], 0])
    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]
        if not done[cur_node]:
            for e in e_list[cur_node]:
                if dist[e[0]] > dist[cur_node] + e[1]:
                    dist[e[0]] = dist[cur_node] + e[1]
                    heapq.heappush(node_heap, [dist[e[0]], e[0]])
        done[cur_node] = True
    return dist


n, q = map(int, input().split())
l_adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    l_adj[a - 1].append([b - 1, 1])
    l_adj[b - 1].append([a - 1, 1])

dist = dijkstra(n, l_adj)

l_cd = []
for _ in range(q):
    c, d = map(int, input().split())
    l_cd.append([c - 1, d - 1])

for cd in l_cd:
    c = cd[0]
    d = cd[1]
    dist_c = dist[c]
    dist_d = dist[d]
    if abs(dist_c - dist_d) % 2 == 0:
        print('Town')
    else:
        print('Road')
