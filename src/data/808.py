import sys

sys.setrecursionlimit(10**6)
N, Q = map(int, input().split())
graph = [[] for i in range(N)]
ans = [0] * N
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(v, pre, flag):
    ans[v] = flag
    for e in graph[v]:
        if e == pre: continue
        dfs(e, v, (flag + 1) % 2)


dfs(0, -1, 0)
#print(ans)
for _ in range(Q):
    c, d = map(int, input().split())
    if ans[c - 1] == ans[d - 1]: print("Town")
    else: print("Road")
