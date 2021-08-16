from collections import deque

N, Q = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    matrix[a - 1].append(b - 1)
    matrix[b - 1].append(a - 1)
    matrix[i].append(i)

visited = [0 for _ in range(N)]
visited[0] = 1
d = deque([0])
cost = 1
cost_matrix = [1e9 for _ in range(N)]
cost_matrix[0] = 0
while d:
    for _ in range(len(d)):
        place = d.popleft()
        for i in matrix[place]:
            if not visited[i]:
                visited[i] = 1
                d.append(i)
                cost_matrix[i] = cost
    cost += 1
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (cost_matrix[c] + cost_matrix[d]) % 2 == 1:
        print('Road')
    else:
        print('Town')
