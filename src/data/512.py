import sys

sys.setrecursionlimit(10**6)
N, Q = map(int, input().split())
adj = [[] for _ in range(N)]
nodes = [-1 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


def dfs(v, flag):
    global nodes
    nodes[v] = flag
    flag ^= 1
    for to in adj[v]:
        if nodes[to] == -1:
            dfs(to, flag)


dfs(0, 0)

for _ in range(Q):
    c, d = map(int, input().split())
    if (nodes[c - 1] + nodes[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
