import sys

sys.setrecursionlimit(100000)

n, q = map(int, input().split())
g = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)


def dfs(v, depth):
    if temp[v]:
        return
    temp[v] = True
    depth += 1
    #print(depth)
    dep[v] = depth
    for vv in g[v]:
        dfs(vv, depth)


temp = [False] * n
dep = [0] * n
dfs(0, 0)

#print(dep)
ans = []
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(dep[d] - dep[c]) % 2 == 0:
        print('Town')
    else:
        print('Road')
