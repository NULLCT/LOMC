import sys

sys.setrecursionlimit(100000)
N, Q = map(int, input().split())

towns = [-1] * N

ways = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    ways[a - 1].append(b - 1)
    ways[b - 1].append(a - 1)


def DFS(town, zero_one):
    towns[town] = zero_one
    for to in ways[town]:
        if towns[to] != -1:
            continue
        DFS(to, (zero_one + 1) % 2)


DFS(0, 0)

for _ in range(Q):
    c, d = map(int, input().split())
    print("Town" if towns[c - 1] == towns[d - 1] else "Road")
