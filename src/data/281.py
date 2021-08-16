import sys

sys.setrecursionlimit(10**6)

G = [[] for _ in range(100100)]
check = [0 for _ in range(100100)]
col = [0 for _ in range(100100)]


def dfs(now, x):
    check[now] = 1
    col[now] = x
    for i in G[now]:
        if check[i] == 0:
            x ^= 1
            dfs(i, x)
            x ^= 1
    return


def main():
    n, q = map(int, input().split())
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    dfs(0, 0)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        print("Road" if col[c] != col[d] else "Town")
    return


main()
