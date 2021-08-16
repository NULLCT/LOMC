import sys, os

sys.setrecursionlimit(1000000)


def debug(*args, **kwargs):
    if os.getenv('DEBUG'):
        print(*args, **kwargs, file=sys.stderr)


def input():
    return sys.stdin.readline()[:-1]


def int0(s: str) -> int:
    return int(s) - 1


def main(_=0):
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int0, input().split())
        G[a].append(b)
        G[b].append(a)

    INF = 1001001001
    dist = [INF] * N
    dist[0] = 0
    P = [-1] * N

    def dfs(v, p, d):
        P[v] = d
        dist[v] = d
        for u in G[v]:
            if u == p: continue
            dfs(u, v, 1 + d)

    dfs(0, -1, 0)

    # doubling
    k = len(bin(max(dist))[2:])
    dbl = [[-1] * N for _ in range(k + 1)]
    for i in range(N):
        dbl[0][i] = P[i]
    for i in range(k):
        for j in range(N):
            if dbl[i][j] == -1: continue
            dbl[i + 1][j] = dbl[i][dbl[i][j]]

    ## (1) u, v の深さが同じになるまでお互い登っていく
    ## (2) 頂点が同じになる直前まで登っていく
    def lca(u, v):
        ## u のほうを深くする
        if dist[u] <= dist[v]:
            u, v = v, u
        if dist[u] != dist[v]:
            ## 深さの差
            d = dist[u] - dist[v]
            for i in range(k):
                if (d >> i) & 1:
                    u = dbl[i][u]
        if u == v: return u
        for i in range(k, -1, -1):
            if dbl[i][u] != dbl[i][v]:
                u, v = dbl[i][u], dbl[i][v]
        return dbl[0][u]

    # LCA がわかれば一瞬
    for _ in range(Q):
        c, d = map(int0, input().split())
        p = lca(c, d)
        D = 1 + dist[c] + dist[d] - (2 * dist[p])

        if D % 2 == 0:
            print("Road")
        else:
            print("Town")


def as_input(s: str) -> None:
    import io
    global input
    f = io.StringIO(s)
    input = lambda: f.readline().rstrip()
    return None


sample1 = """4 1
1 2
2 3
2 4
1 2
"""
sample2 = """5 2
1 2
2 3
3 4
4 5
1 3
1 5
"""
sample3 = """9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6
"""


def test():
    """
    >>> main(as_input(sample1))
    Road
    >>> main(as_input(sample2))
    Town
    Town
    >>> main(as_input(sample3))
    Town
    Road
    Town
    Town
    Town
    Town
    Road
    Road
    Road
    """
    pass


if __name__ == '__main__':
    main()
