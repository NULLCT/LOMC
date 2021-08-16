from collections import defaultdict
import queue
import sys

sys.setrecursionlimit(10**9)

#r = defaultdict(list)
n, q = map(int, input().split())
r = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    #r[a].append(b)
    #r[b].append(a)
    r[a].append(b)
    r[b].append(a)

tr = [-1] * (n + 1)


def dfs(parent, current):
    tr[current] = (tr[parent] + 1) % 2
    for v in r[current]:
        if tr[v] == -1:
            dfs(current, v)


dfs(0, 1)
for i in range(q):
    c, d = map(int, input().split())
    if tr[c] == tr[d]:
        print("Town")
    else:
        print("Road")
