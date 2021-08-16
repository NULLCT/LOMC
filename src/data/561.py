from collections import deque


# 二部グラフの色を出力する関数
def bfs(N, G, s):
    color = [-1] * N  # 黒は1,白は0,未探索は-1
    q = deque()
    color[s] = 1
    q.appendleft(s)
    while q:
        v = q[-1]
        q.pop()
        for x in G[v]:
            if color[x] != -1: continue  # 探索済
            # color[v]が1ならcolor[x]は0,color[v]が0ならcolor[x]は1
            color[x] = 1 - color[v]
            q.appendleft(x)
    return color


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

Query = []
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    Query.append([c, d])

color = bfs(N, G, 0)
# print(color)

for q in Query:
    # 同じ色なら距離は偶数、ちがう色なら距離は奇数
    if color[q[0]] == color[q[1]]:
        print('Town')
    else:
        print('Road')
