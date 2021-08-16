import sys

sys.setrecursionlimit(10**6)


def inp(dtype=int):
    return list(map(dtype, input().split()))


N, Q = inp()
a, b = zip(*[inp() for _ in range(N - 1)])

tree = [[] for _ in range(N + 1)]
for i, j in zip(a, b):
    tree[i].append(j)
    tree[j].append(i)

dist = [0 for _ in range(N + 1)]


def dfs(i=1, prev=0):
    for j in tree[i]:
        if j == prev:
            continue
        dist[j] = dist[i] + 1
        dfs(j, i)


dfs()
for _ in range(Q):
    c, d = inp()
    if (dist[c] - dist[d]) % 2:
        print("Road")
    else:
        print("Town")
