import heapq

n, q = map(int, input().split())
A, B, C, D = [], [], [], []

for _ in range(n - 1):
    a, b = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)

for _ in range(q):
    c, d = map(int, input().split())
    C.append(c - 1)
    D.append(d - 1)

e = [[] for _ in range(n)]
for i in range(n - 1):
    e[A[i]].append((1, B[i]))
    e[B[i]].append((1, A[i]))


def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)  # リストを優先度付きキューに変換
    cost = [10**6 + 1] * n  # 行ったことのないところはinf
    cost[s] = 0  # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:  # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost


cost = dijkstra(0)

for i in range(q):
    if cost[C[i]] % 2 == cost[D[i]] % 2:
        print('Town')
    else:
        print('Road')
