import sys

sys.setrecursionlimit(10**9)
N, Q = map(int, input().split())
L = [[] * N for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)

town_color = [-1] * N
town_color[0] = 0


def func(n):
    for l in L[n]:
        if town_color[l] == -1:
            if town_color[n] == 0:
                town_color[l] = 1
            else:
                town_color[l] = 0
            func(l)
        else:
            continue


for l in L[0]:
    town_color[l] = 1
    func(l)

for _ in range(Q):
    c, d = map(int, input().split())
    if town_color[c - 1] == town_color[d - 1]:
        print('Town')
    else:
        print('Road')
