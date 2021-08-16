#!/usr/bin/env python3
import sys

sys.setrecursionlimit(200_000)


def solve(N, Q, AB, CD):
    edges = [[] for _ in range(N + 1)]
    for a, b in AB:
        edges[a].append(b)
        edges[b].append(a)

    depth = [None] * (N + 1)

    def dfs(cur, d):
        if depth[cur] is not None:
            return
        depth[cur] = d
        for nex in edges[cur]:
            dfs(nex, d + 1)

    dfs(1, 0)

    for c, d in CD:
        if abs(depth[c] - depth[d]) % 2 == 0:
            yield "Town"
        else:
            yield "Road"


def main():
    N, Q = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N - 1)]
    CD = [tuple(map(int, input().split())) for _ in range(Q)]
    print(*solve(N, Q, AB, CD), sep="\n")


if __name__ == '__main__':
    main()
