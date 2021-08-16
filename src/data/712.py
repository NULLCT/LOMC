from collections import deque


def adjlist(n, edges, digraph=False):
    adj = [set() for _ in range(n + 1)]

    if digraph:
        for s, t in edges:
            adj[s].add(t)
    else:
        for s, t in edges:
            adj[s].add(t)
            adj[t].add(s)

    return adj


def tmap(fn, seq):
    return tuple(map(fn, seq))


def solve():
    N, Q = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(N - 1)]
    qs = [tmap(int, input().split()) for _ in range(Q)]
    # print(N, Q, E, qs)

    adj = adjlist(N, E)

    todo = deque([1])
    seen = [False] * (N + 1)
    color = [True] * (N + 1)

    while todo:
        v = todo.pop()
        seen[v] = True
        for t in adj[v]:
            if not seen[t]:
                todo.appendleft(t)
                color[t] = not color[v]

    for c, d in qs:
        if color[c] == color[d]:
            print("Town")
        else:
            print("Road")


solve()
