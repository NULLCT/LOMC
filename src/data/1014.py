import sys, math

sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()


def li():
    return list(map(int, input().split()))


N, Q = li()
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = li()
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

from collections import deque


def dfs(start, num_node):
    stack = [start]
    seen = [False] * (num_node)
    seen[start] = 1
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if seen[y]:
                continue
            stack.append(y)
            seen[y] = seen[x] + 1
    return seen


dist = dfs(0, N)
for _ in range(Q):
    a, b = li()
    a -= 1
    b -= 1
    if (dist[a] + dist[b]) % 2 == 1:
        print('Road')
    else:
        print('Town')
