from collections import deque

N, Q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N - 1)]
adjacent = [[] for _ in range(N + 1)]
for a, b in ab:
    adjacent[a].append(b)
    adjacent[b].append(a)
cd = [tuple(map(int, input().split())) for _ in range(Q)]

# ノード1からの距離の偶奇で二分木を塗り分け
dist = [-1] * (N + 1)
q = deque([1])
dist[1] = 0
while q:
    city = q.popleft()
    for n in adjacent[city]:
        if dist[n] < 0:
            dist[n] = 1 + dist[city]
            q.append(n)
# キューの処理
for c, d in cd:
    p = "Town" if (dist[c] + dist[d]) % 2 == 0 else "Road"
    print(p)
