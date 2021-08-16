import sys

sys.setrecursionlimit(200000000)
n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
s = [0] * n


def DFS(i):
    s[i] = 1
    for ni in graph[i]:
        if not s[ni]:
            return DFS(ni)
    return i


x = DFS(0)
d = [float('inf')] * n
d[x] = 0


def dfs(i):
    for ni in graph[i]:
        if d[ni] == float('inf'):
            d[ni] = d[i] + 1
            dfs(ni)


dfs(x)
for _ in range(q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    if (d[p] - d[q]) % 2:
        print('Road')
    else:
        print('Town')
