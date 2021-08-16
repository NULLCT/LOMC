import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)


def dfs(vs):
    for ve in edge[vs]:
        if even_odd[ve] > -1: continue
        even_odd[ve] = even_odd[vs] ^ 1
        dfs(ve)


even_odd = [-1] * n
even_odd[0] = 0
dfs(0)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if even_odd[c] == even_odd[d]: print("Town")
    else: print("Road")
