import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
edge = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

ps = [0] * N
used = [False] * N


def dfs(frm):
    for to in edge[frm]:
        if used[to]: continue
        ps[to] = ps[frm] + 1
        used[to] = True
        dfs(to)
    return


dfs(0)

for q in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (ps[c] + ps[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
