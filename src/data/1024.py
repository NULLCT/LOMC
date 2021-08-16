import sys

sys.setrecursionlimit(200005)


def dfs(sommet, parent):
    global dist
    global adj
    for v in adj[sommet]:
        if v != parent:
            dist[v] = 1 + dist[sommet]
            dfs(v, sommet)


n, q = map(int, input().split())
adj = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a] += [b]
    adj[b] += [a]

dist = [0] * (n + 1)

dfs(1, -1)
# ~ print("dist", dist)
for _ in range(q):
    a, b = map(int, input().split())
    r = dist[a] + dist[b]
    print("Town" if r % 2 == 0 else "Road")
