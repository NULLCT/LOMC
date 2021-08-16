N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

from collections import defaultdict

adj = defaultdict(set)
for a, b in ab:
    adj[a - 1].add(b - 1)
    adj[b - 1].add(a - 1)

from collections import deque

INF = float('inf')


def bfs(start):
    todo = deque()
    todo.append((0, start))  # 初期探索場所をpush
    dists = [INF] * N

    while len(todo) > 0:
        dist, pos = todo.popleft()  # FIFOでpop
        if dists[pos] < INF:
            continue
        dists[pos] = dist

        # 次の位置を探索する
        for next_ in adj[pos]:
            todo.append((dist + 1, next_))
    return dists


dists = bfs(0)

for c, d in cd:
    ans = dists[c - 1] + dists[d - 1]
    print('Road' if ans % 2 == 1 else 'Town')
