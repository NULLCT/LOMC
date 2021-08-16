import sys

read = sys.stdin.read
sys.setrecursionlimit(10**6)
from collections import defaultdict


def main():
    def dfs(prev, v, di):
        dis[v] = di
        for nv in g[v]:
            if nv != prev:
                dfs(v, nv, di + 1)

    n, q = map(int, input().split())

    g = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append(b)
        g[b].append(a)
    dis = [0] * n
    dfs(-1, 0, 0)
    for _ in range(q):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        d2 = dis[c] + dis[d]
        if d2 & 1:
            print('Road')
        else:
            print('Town')


if __name__ == '__main__':
    main()
