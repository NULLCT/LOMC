import sys  #追加

sys.setrecursionlimit(500 * 500)  #追加
from collections import deque

n, q = map(int, input().split())
road = [[] * n for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)
d = deque()
d.append(0)
visit = [-1] * n
judge = 0


def dfs(v, judge):
    if visit[v] != -1:
        return
    visit[v] = judge
    for i in road[v]:
        dfs(i, 1 - judge)
    return


dfs(0, judge)
for i in range(q):
    c, d = map(int, input().split())
    if visit[c - 1] == visit[d - 1]:
        print("Town")
    else:
        print("Road")
