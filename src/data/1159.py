import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
seen = [0 for _ in range(n)]
tr = [0 for _ in range(n)]


def dfs(x, hu):
    seen[x] = 1
    tr[x] = hu
    for i in graph[x]:
        if seen[i]: continue
        dfs(i, hu + 1)


dfs(0, 0)
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (tr[c] - tr[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
