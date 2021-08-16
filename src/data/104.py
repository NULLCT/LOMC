# D after contest
from collections import deque, defaultdict

N, Q = map(int, input().split())

edges = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    # 訪問済み、または、これから訪れる頂点部分集合
    C = set()
    C.add(start)
    distances[start] = 0

    while q:
        v = q.popleft()
        for each in edges[v]:
            if each not in C:
                C.add(each)
                q.append(each)
                distances[each] = distances[v] + 1


# 最短経路リスト
distances = [-1] * (N + 1)
# スタート地点からの最短距離をもれなく更新
bfs(1)

while Q:
    Q -= 1
    c, d = map(int, input().split())
    print('Town' if abs(distances[c] - distances[d]) % 2 == 0 else 'Road')
