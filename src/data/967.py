from sys import stdin

n, q = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)
colors = [0] * n


def is_bipartite():
    stack = [(0, 1)]  # (頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        v, color = stack.pop()
        colors[v] = color
        for to in edge[v]:
            if colors[to] == color:
                return False
            if colors[to] == 0:
                stack.append((to, -color))
    return True


is_bipartite()

for _ in range(q):
    c, d = map(int, stdin.readline().split())
    s = colors[c - 1]
    t = colors[d - 1]

    if s == t:
        print('Town')
    else:
        print('Road')
