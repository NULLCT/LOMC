N, Q = map(int, input().split())

from collections import deque

que = deque()

#いけるとこリスト
connect = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

#いったとこリスト
visited = [False] * (N + 1)

counter = [-1] * (N + 1)

que.append(1)
visited[1] = True

while que:
    now = que.popleft()

    for to in connect[now]:
        if visited[to] == False:
            counter[to] += 1 - counter[now]
            visited[to] = True
            que.append(to)
#訪問済みリストを初期化
visited = [False] * (N + 1)

for i in range(Q):
    a, b = map(int, input().split())
    if counter[a] == counter[b]:
        print('Town')

    else:
        print('Road')
