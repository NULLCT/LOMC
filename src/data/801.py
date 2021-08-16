n, q = [int(_) for _ in input().split()]
lis = [[] for i in range(n)]
import sys

sys.setrecursionlimit(10**5 + 10)

for i in range(n - 1):
    a, b = [int(_) - 1 for _ in input().split()]
    lis[a].append(b)
    lis[b].append(a)

g = [-1 for i in range(n)]
g[0] = 1


def set(x):
    for i in lis[x]:
        if g[i] == -1:
            g[i] = (g[x] % 2) + 1
            set(i)
    return


set(0)

for i in range(q):
    c, d = [int(_) - 1 for _ in input().split()]
    if g[c] == g[d]:
        print("Town")
    else:
        print("Road")