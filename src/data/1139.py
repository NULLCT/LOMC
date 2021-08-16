import collections
import sys

sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n - 1)]
    cd = [tuple(map(int, input().split())) for _ in range(q)]

    G = {}
    col = collections.Counter()

    #1. Input
    for a, b in ab:
        if a not in G.keys():
            G[a] = [b]
        else:
            G[a].append(b)
        if b not in G.keys():
            G[b] = [a]
        else:
            G[b].append(a)

    for a, b in ab:
        G[a].append(b)
        G[b].append(a)

    def dfs(pos, cur):
        col[pos] = cur
        for i in G[pos]:
            if (col[i] >= 1):
                continue
            dfs(i, 3 - cur)

#2. Graph Coloring

    dfs(1, 1)

    for c, d in cd:
        if col[c] == col[d]:
            print('Town')
        else:
            print('Road')

    return 0

if __name__ == '__main__':
    main()
