import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
Tree = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Tree[a].append(b)  # 次の頂点
    Tree[b].append(a)

d = [0] * N  # 根からの距離
parent = [-1] * N


def dfs(v, p=-1):
    # v: 子, p: 親
    parent[v] = p
    for u in Tree[v]:
        # u: 行き先
        if u == p:
            continue
        d[u] += d[v] + 1
        dfs(u, v)


dfs(0)
out = []
for i in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if abs(d[a] - d[b]) % 2 == 1:
        out.append("Road")
    else:
        out.append("Town")
print(*out, sep="\n")
