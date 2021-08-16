#ABC_209
#D
from collections import deque

n, q = map(int, input().split())
R = [[] for _ in range(n)]  #経路情報
for _ in range(n - 1):
    r1, r2 = map(int, input().split())
    r1 -= 1
    r2 -= 1
    R[r1].append(r2)
    R[r2].append(r1)

query = list()  #クエリ情報
for _ in range(q):
    q1, q2 = map(int, input().split())
    q1 -= 1
    q2 -= 1
    query.append([q1, q2])

dist = [-1 for _ in range(n)]
Q = deque()
Q.append((0, 0))  #ノード0を視点として各ノードへの距離を計算する
#キューの中で距離の処理をしていく
while len(Q) > 0:
    (node, depth) = Q.popleft()
    if dist[node] == -1:
        dist[node] = depth
    for child in R[node]:
        if dist[child] == -1:
            Q.append((child, depth + 1))

for c, d in query:
    if dist[c] % 2 == 0 and dist[d] % 2 == 0:
        ans = "Town"
    elif dist[c] % 2 != 0 and dist[d] % 2 != 0:
        ans = "Town"
    else:
        ans = "Road"
    print(ans)
