import sys

sys.setrecursionlimit(10**9)
N, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
#rint(tree)

depth = [-1] * (N + 1)


def dfs0(u, d):
    depth[u] = d
    for v in tree[u]:
        if depth[v] == -1:
            dfs0(v, 1 - d)


dfs0(1, 0)

#rint(depth)
for _ in range(Q):
    c, d = map(int, input().split())
    length = depth[d] - depth[c]
    if length % 2 == 0:
        print("Town")
    else:
        print("Road")
