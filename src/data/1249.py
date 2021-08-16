from math import modf, pi, gcd
from heapq import heappop, heappush
from collections import deque

INF = 1 << 60
MOD = 10**9 + 7
# MOD = 998244353


def main():
    n, Q = map(int, input().split())
    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        path[a - 1].append(b - 1)
        path[b - 1].append(a - 1)
    q = deque()
    q.append(0)
    visited = [-1] * n
    visited[0] = 0
    while len(q) > 0:
        x = q.popleft()
        for nx in path[x]:
            if visited[nx] >= 0:
                continue
            visited[nx] = visited[x] + 1
            q.append(nx)
    ret = []
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1

        tmp = visited[c] + visited[d]
        if tmp % 2 == 0:
            ret.append('Town')
        else:
            ret.append('Road')
    for v in ret:
        print(v)


def dijkstra(s, n, adj):  # (始点, ノード数, 道グラフ)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


def warshallFloyd(path):
    n = len(path)
    cost = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j, c in path[i]:
            cost[i][j] = c
        cost[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost


if __name__ == "__main__":
    main()
