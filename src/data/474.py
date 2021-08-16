import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
p = [0]
flg = [True] * N
pnt = 0
cnt = 1
color = [-1] * N
color[0] = 0
while pnt < cnt:
    n = cnt
    for i in range(pnt, cnt):
        c = p[i]
        for j in graph[c]:
            if flg[j]:
                flg[j] = False
                p.append(j)
                color[j] = 1 - color[c]
                cnt += 1
    pnt = n
for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
