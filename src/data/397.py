import sys

sys.setrecursionlimit(10**8)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

color = [-1] * N
color[0] = 0


def set_color_around(i):
    for to in g[i]:
        if color[to] != -1:
            continue
        color[to] = not color[i]
        set_color_around(to)


set_color_around(0)

for c, d in CD:
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
