import logging
import sys
from inspect import currentframe

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

logging.basicConfig(level=logging.DEBUG)


def dbg(*args):
    id2names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    logging.debug(", ".join(
        id2names.get(id(arg), "???") + " = " + repr(arg) for arg in args))


n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
d = [-1] * n
d[0] = 0


def dfs(v, p=-1):
    for nv in g[v]:
        if nv == p:
            continue
        d[nv] = d[v] + 1
        dfs(nv, v)


dfs(0)
# print(d)
maxi = -1
maxd = -1
for i in range(n):
    if d[i] > maxd:
        maxd = d[i]
        maxi = i
# print(maxi, maxd)
d2 = [-1] * n
d2[maxi] = 0


def dfs2(v, p=-1):
    for nv in g[v]:
        if nv == p:
            continue
        d2[nv] = d2[v] + 1
        dfs2(nv, v)


dfs2(maxi)
# print(d2)
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    dist = abs(d2[c] - d2[d])
    if dist & 1:
        print("Road")
    else:
        print("Town")
