"""
街1からの最短距離が偶数か奇数かで考える.
すると偶数の街から奇数の街へまたは,奇数の街から偶数の街への移動のみとなる.
よってスタートする街が偶数か奇数かが異なっていれば同じ街で会うことはなく,
逆に同じであれば道路で会うことはない.
スタート地点が偶数か奇数かを調べるのみで判定可能なため計算量はO(1*q)=O(q)となる.
"""
from collections import deque

n, q = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n - 1)]
cdl = [list(map(int, input().split())) for _ in range(q)]
graph = [[] for _ in range(n + 1)]  # graph[i]: iから繋がっている街一覧(graph[0]不使用)
for a, b in abl:
    graph[a].append(b)
    graph[b].append(a)
dist = [-1] * (n + 1)  # 街1からの距離が偶数か奇数かを記憶
dist[0] = 0  # 不使用
dist[1] = 0  # 街1は街1から0(偶数)
dq = deque([1])
while dq:
    v = dq.popleft()
    for i in graph[v]:
        if dist[i] == -1:
            dist[i] = 1 - dist[v]
            dq.append(i)
for c, d in cdl:
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
