import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())
    g = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    dist = [-1] * n
    seen = [False] * n
    dist[0] = 0

    def dfs(i):
        if seen[i]: return
        seen[i] = True
        for j in g[i]:
            dist[j] = (dist[i] + 1) % 2
            dfs(j)

    dfs(0)
    for i in range(q):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        if dist[c] == dist[d]:
            print('Town')
        else:
            print('Road')


main()
