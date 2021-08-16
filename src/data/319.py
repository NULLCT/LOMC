import sys

sys.setrecursionlimit(10**9)
city, Q = map(int, input().split())
road = [[] for i in range(city)]
flag = [-1] * (city)
for i in range(city - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)
flag[0] = 0


def dfs(x):
    for i in road[x]:
        if flag[i] == -1:
            if flag[x] == 0:
                flag[i] = 1
            elif flag[x] == 1:
                flag[i] = 0
            dfs(i)
    return 0


dfs(0)
Queri = [0] * Q
for i in range(Q):
    Queri[i] = list(map(int, input().split()))
for i in range(Q):
    if flag[Queri[i][0] - 1] == flag[Queri[i][1] - 1]:
        print("Town")
    else:
        print("Road")
