import sys
from functools import lru_cache
from collections import defaultdict

sys.setrecursionlimit(500005)


def get_line_int():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_line_float():
    return list(map(float, sys.stdin.readline().strip().split()))


def in1():
    return int(input())


MAXN, MAXQ = 100100, 20

g = defaultdict(list)
tin = defaultdict(int)
tout = defaultdict(int)
d = defaultdict(int)
up = [[0] * MAXQ for _ in range(MAXN)]

timer = 0
root = 0


def visit(pa, u: int):
    global timer
    timer += 1
    d[u] = d[pa] + 1
    tin[u] = timer
    up[u][0] = pa
    for i in range(1, MAXQ):
        up[u][i] = up[up[u][i - 1]][i - 1]

    for v in g[u]:
        if v != pa:
            visit(u, v)

    timer += 1
    tout[u] = timer


def is_ancestor(a, b: int) -> bool:
    return tin[a] <= tin[b] and tout[a] >= tout[b]


def get_lca(a, b: int) -> int:
    if is_ancestor(a, b):
        return a
    elif is_ancestor(b, a):
        return b
    else:
        for i in range(MAXQ - 1, -1, -1):
            if not is_ancestor(up[a][i], b):
                a = up[a][i]

        return up[a][0]


n, q = get_line_int()

for i in range(n - 1):
    u, v = get_line_int()
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

visit(0, 0)

for i in range(q):
    a, b = get_line_int()
    a, b = a - 1, b - 1

    l = get_lca(a, b)
    sz = d[a] + d[b] - 2 * d[l] + 1
    if sz % 2 == 0:
        print("Road")
    else:
        print("Town")
