import sys
import heapq


def dijkstra(graph, start, n):
    INF = 10**18
    hq = [(start, 0)]
    heapq.heapify(hq)
    cost = [INF] * n
    cost[start] = 0
    while hq:
        v, c = heapq.heappop(hq)
        if c > cost[v]:  #更新なし
            continue
        for idx, d in graph[v]:
            if d + cost[v] < cost[idx]:
                cost[idx] = d + cost[v]
                heapq.heappush(hq, (idx, d + cost[v]))

    return cost


def main():
    n, q = map(int, input().split())
    city = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        city[a - 1].append((b - 1, 1))
        city[b - 1].append((a - 1, 1))

    dist_start = dijkstra(city, 0, n)

    for i in range(q):
        c, d = map(int, input().split())
        dist_c = dist_start[c - 1]
        dist_d = dist_start[d - 1]

        if (dist_c + dist_d) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
