II = lambda: int(input())
MI = lambda: map(int, input().split())
OI = lambda: map(int, open(0).read().split())

#隣接リスト作成
N, Q = map(int, input().split())
G = [[] for _ in range(N)]  #隣接リスト
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

#DFS/BFS 非再帰
from collections import deque

i_init, v_init, v_yet = 0, 0, -1
D = deque()
D.appendleft([i_init, v_init])
V = [v_yet] * N
V[i_init] = v_init

#探索
while D:
    i, v = D.popleft()
    for j in G[i]:
        if V[j] == v_yet:
            v_new = 1 - v
            V[j] = v_new
            D.appendleft([j, v_new])

for _ in range(Q):
    a, b = map(int, input().split())
    print(('Road', 'Town')[V[a - 1] == V[b - 1]])
