from collections import deque

n, q = map(int, input().split())

#グラフ
l = [[] for i in range(n)]
#次の目的地管理
dq = deque()
#スタートからの距離と訪問/未訪問を同時管理
dist = [-1] * n

for i in range(n - 1):
    a, b = map(int, input().split())
    l[a - 1].append(b - 1)
    l[b - 1].append(a - 1)

#幅優先探索はゴールだけに結果を求めるのではなく、
#スタート地点からの最短距離をスタート地点以外のすべての頂点について記録し、
#あとからゴール地点を検索する
dq.append(0)
dist[0] = 0
while len(dq) > 0:
    s = dq.popleft()
    for j in l[s]:
        if dist[j] == -1:
            dist[j] = dist[s] + 1
            dq.append(j)

for i in range(q):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print('Town')
    else:
        print('Road')
