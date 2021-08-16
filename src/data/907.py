from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)
n, q = map(int, (input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    ai, bi = map(int, input().split())
    graph[ai].append(bi)
    graph[bi].append(ai)
vis = [0] * (n + 1)
dp = [0] * (n + 1)


def dfs(node, val):
    vis[node] = 1
    for child in graph[node]:
        if vis[child] == 0:
            dfs(child, val + 1)
    dp[node] = val


dfs(1, 0)
for _ in range(q):
    ci, di = map(int, input().split())
    if (dp[di] - dp[ci]) % 2: print("Road")
    else: print("Town")
