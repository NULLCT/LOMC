#!python3

import sys
from collections import defaultdict, deque

iim = lambda: map(int, sys.stdin.readline().rstrip().split())


def resolve():
    it = map(int, sys.stdin.read().split())
    N, Q = next(it), next(it)

    inf = float("inf")
    d1 = defaultdict(list)
    for i in range(N - 1):
        a, b = next(it) - 1, next(it) - 1
        d1[a].append(b)
        d1[b].append(a)

    ds = [0] * N

    def dfs(i, d=0):
        vis[i] = 1
        ds[i] = d
        for j in d1[i]:
            if vis[j]: continue
            dfs(j, d + 1)

    dq = deque([(0, 1)])
    while dq:
        i, d = dq.pop()

        ds[i] = d
        for j in d1[i]:
            if ds[j]: continue
            dq.append((j, d + 1))

    ans = []
    for i in range(Q):
        a, b = next(it) - 1, next(it) - 1
        c = ds[a] + ds[b]
        ans.append("Road" if c % 2 else "Town")

    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()
