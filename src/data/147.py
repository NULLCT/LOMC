def init_arg(num):
    return int(num) - 1


def II():
    return int(input())


def IS():
    return input()


def IL():
    return list(map(int, input().split()))


def IL_arg():
    return list(map(init_arg, input().split()))


def ILs(n):
    return [list(map(int, input().split())) for _ in range(n)]


tf = lambda boolean: "Yes" if boolean else "No"


def INF():
    return 1e10


def zeros1(n):
    return [0 for _ in range(n)]


def zeros2(n, m):
    return [[0 for _ in range(n)] for _ in range(m)]


import sys

sys.setrecursionlimit(2 * 10**9)

n, q = IL()

adjs = [[] for _ in range(n)]
reached = [0 for _ in range(n)]
colors = [INF() for _ in range(n)]
for _ in range(n - 1):
    a, b = IL()
    a -= 1
    b -= 1
    adjs[a].append(b)
    adjs[b].append(a)


def dfs(node, depth=1):
    reached[node] = 1
    colors[node] = depth % 2

    for adjnode in adjs[node]:
        # 未探索であれば
        if reached[adjnode] == 0:
            reached[adjnode] = 1
            dfs(adjnode, depth + 1)


dfs(0)
for _ in range(q):
    c, d = IL()
    c -= 1
    d -= 1
    if colors[c] == colors[d]:
        print("Town")
    else:
        print("Road")
