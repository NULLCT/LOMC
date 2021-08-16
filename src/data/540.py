from sys import stdin

input = stdin.readline

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    G[x].append(y)
    G[y].append(x)


def bfs(graph, start):
    from collections import deque
    seen = [False] * len(graph)
    todo = deque()
    color = [0] * len(graph)

    seen[start] = True
    todo.append(start)
    color[start] = 1

    while todo:
        v = todo.popleft()
        for w in graph[v]:
            if seen[w]: continue
            seen[w] = True
            todo.append(w)
            color[w] = color[v] * (-1)

    return color


color = bfs(G, 0)

for q in range(Q):
    c, d = map(lambda n: int(n) - 1, input().split())
    print("Town" if color[c] == color[d] else "Road")
