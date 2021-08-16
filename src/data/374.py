import sys
import resource

sys.setrecursionlimit(10**6)
N, Q = map(int, input().split())
INF = 10**18

edge = [[] for _ in range(N)]

for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    edge[B].append(A)
dep = [0] * N


def dfs(now, last=-1):
    for next in edge[now]:
        if next == last:
            continue
        dep[next] = dep[now] + 1
        dfs(next, now)


dfs(1)
for i in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if (dep[a] + dep[b]) % 2 == 0:
        print("Town")
    else:
        print("Road")
