import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

edge = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    edge[a].append(b)
    edge[b].append(a)
INF = 1 << 63
dist = [INF] * N
dist[0] = 0
visit = [0] * N
# 街0から奇数で到達できる街を1とする
q = [0]
while q:
    i = q.pop()
    if visit[i]: continue
    visit[i] = 1
    for to in edge[i]:
        dist[to] = min(dist[to], dist[i] + 1)
        q.append(to)
# print(dist)
# print(visit)
for i in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
