import sys

sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline()[:-1]


def main():

    N, Q = map(int, input().split())
    G = [list() for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    S = []
    F = [0] * N
    depth = [0] * N
    check = [False] * N

    def dfs(v, d):
        F[v] = len(S)
        depth[v] = d
        S.append(v)
        check[v] = True
        for w in G[v]:
            if not check[w]:
                dfs(w, d + 1)
                S.append(v)

    dfs(0, 0)

    INF = (N, None)

    M = 2 * N
    M0 = 2**(M - 1).bit_length()
    data = [INF] * (2 * M0)
    for i, v in enumerate(S):
        data[M0 - 1 + i] = (depth[v], i)
    for i in range(M0 - 2, -1, -1):
        data[i] = min(data[2 * i + 1], data[2 * i + 2])

    def _query(a, b):
        yield INF
        a += M0
        b += M0
        while a < b:
            if b & 1:
                b -= 1
                yield data[b - 1]
            if a & 1:
                yield data[a - 1]
                a += 1
            a >>= 1
            b >>= 1

    def query(u, v):
        fu = F[u]
        fv = F[v]
        if fu > fv:
            fu, fv = fv, fu
        return S[min(_query(fu, fv + 1))[1]]

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        lca = query(c, d)
        dist = (depth[lca] - depth[c]) + (depth[lca] - depth[d])
        if dist % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
