import sys
from itertools import islice
from typing import NamedTuple
from heapq import heappop, heappush

INF = 1 << 60


def _dijkstra1(N, S, graph):
    queue = []
    dist = [INF] * N
    dist[S] = 0
    queue.append((dist[S], S))

    while queue:
        min_dist, min_v = heappop(queue)
        if min_dist > dist[min_v]:
            continue

        for e in graph[min_v]:
            c = dist[min_v] + 1
            if dist[e] > c:
                dist[e] = c
                heappush(queue, (c, e))

    return dist


def solve(in_):
    N, Q = map(int, next(in_).split())
    graph = [[] for _ in range(N)]
    _edges = tuple(map(int, line.split()) for line in islice(in_, N - 1))
    for a, b in _edges:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    queries = tuple(map(int, line.split()) for line in islice(in_, Q))
    ans = []
    _dist = _dijkstra1(N, 0, graph)
    for c, d in queries:
        c -= 1
        d -= 1
        dist = abs(_dist[c] - _dist[d])
        if dist % 2:
            ans.append('Road')
        else:
            ans.append('Town')
    return ans


def main():
    answer = solve(sys.stdin.buffer)
    print('\n'.join(answer))


if __name__ == '__main__':
    main()
