import sys

#Library Info(ACL for Python/Pypy) -> https://github.com/not522/ac-library-python


def input():
    return sys.stdin.readline().rstrip()


DXY = [(0, -1), (1, 0), (0, 1), (-1, 0)]  #L,D,R,Uの順番

sys.setrecursionlimit(500000)

INF = 1 << 64


def main():
    n, q = map(int, input().split())
    g = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    query = [tuple(map(int, input().split())) for i in range(q)]
    dist = [INF] * (n)
    dist[0] = 0

    def dfs(M):
        for adj in g[M]:
            if dist[adj] == INF:
                dist[adj] = dist[M] + 1
                dfs(adj)

    dfs(0)
    for u, v in query:
        u -= 1
        v -= 1
        if (dist[u] - dist[v]) % 2 != 0:
            print("Road")
        else:
            print("Town")
    return 0


if __name__ == "__main__":
    main()
