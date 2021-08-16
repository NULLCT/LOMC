import sys

sys.setrecursionlimit(100000000)


def search(a, v, depth, d):
    for i in v[a]:
        v[i].remove(a)
        depth[i] = d + 1
        search(i, v, depth, d + 1)


N, M = map(int, input().split())
v = [[] for i in range(N)]
depth = [0] * N
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
search(0, v, depth, 0)
for i in range(M):
    a, b = map(int, input().split())
    if (depth[a - 1] - depth[b - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
