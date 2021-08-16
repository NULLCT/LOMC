#!/usr/bin/env python3
import sys
from collections import deque

# import io
# _INPUT = """\
# """
# sys.stdin = io.StringIO(_INPUT)


def input():
    return sys.stdin.readline()[:-1]


def bfs(graph, startV):
    dist = [-1] * len(graph)
    dist[startV] = 0

    que = deque()
    que.append(startV)

    while que:
        curV = que.popleft()

        neighborVs = graph[curV]
        for v in neighborVs:
            # 探索済の場合
            if dist[v] != -1:
                dist[v] = min(dist[v], dist[curV] + 1)
                continue

            que.append(v)
            dist[v] = dist[curV] + 1

    return dist


def main():
    N, Q = map(int, input().split())
    a, b = [0] * N, [0] * N
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N):
        _a, _b = map(int, input().split())
        a[i], b[i] = _a, _b
        graph[_a].append(_b)
        graph[_b].append(_a)

    dist = bfs(graph, 1)
    colors = [0] * (N + 1)
    for i in range(len(dist)):
        if dist[i] % 2 == 0:
            colors[i] = 1

    for i in range(Q):
        c, d = map(int, input().split())

        # 距離が偶数ならRoad、奇数ならTown
        isMeetingInTown = colors[c] == colors[d]
        print('Town' if isMeetingInTown else 'Road')


if __name__ == "__main__":
    main()
