from collections import deque

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
Qn = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N + 1)]
for A, B in AB:
    graph[A].append(B)
    graph[B].append(A)


def BFS():
    q = deque()
    q.append(1)
    cost[1] = 0
    while q:
        p = q.popleft()
        if visit[p]:
            continue
        visit[p] = True
        for p2 in graph[p]:
            if visit[p2]:
                continue
            cost[p2] = cost[p] + 1
            q.append(p2)
    return


visit = [False] * (N + 1)
cost = [-1] * (N + 1)
BFS()

for C, D in Qn:
    if abs(cost[C] - cost[D]) % 2 == 1:
        print('Road')
    else:
        print('Town')
