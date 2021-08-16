from collections import deque


def DFS(now_pos):
    Q = deque()
    Q.append(now_pos)
    cost[now_pos] = 0
    check[now_pos] = True
    while len(Q) > 0:
        pos = Q.popleft()
        for to in box[pos]:
            cost[to] = cost[pos] + 1
            if check[to] == False:
                check[to] = True
                Q.append(to)


N, Q = map(int, input().split())
box = [[] * (N + 2) for _ in range(N + 2)]
for i in range(N - 1):
    a, b = map(int, input().split())
    box[a].append(b)
    box[b].append(a)

cost = [0] * (N + 2)
check = [False] * (N + 2)
DFS(1)
for i in range(Q):
    c, d = map(int, input().split())
    num = cost[d] + cost[c]
    if num % 2 == 0:
        print("Town")
    else:
        print("Road")
