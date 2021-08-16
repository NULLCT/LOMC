import sys

sys.setrecursionlimit(10**8)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dones = [-1] * N


def dfs(now, num, pre):
    dones[now] = num

    num += 1
    num %= 2

    for nex in G[now]:
        if nex == pre:
            continue

        dfs(nex, num, now)


dfs(0, 0, -1)

for i in range(Q):
    c, d = map(int, input().split())
    if dones[c - 1] == dones[d - 1]:
        print("Town")
    else:
        print("Road")
