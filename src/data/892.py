import heapq

N, Q = map(int, input().split())
hq = []
p = [[] for i in range(N)]
lcm = [[] for i in range(N)]
heapq.heapify(hq)
for i in range(N - 1):
    A, B = map(int, input().split())
    p[A - 1].append(B - 1)
    p[B - 1].append(A - 1)
visited = [False for i in range(N)]
score = [float('inf') for i in range(N)]
score[0] = 0
heapq.heappush(hq, [0, 0])
while hq:
    a, b = heapq.heappop(hq)
    if visited[b]:
        continue
    visited[b] = True
    for i in range(len(p[b])):
        if visited[p[b][i]]:
            continue
        d = score[b] + 1
        if d < score[p[b][i]]:
            score[p[b][i]] = d
            heapq.heappush(hq, [d, p[b][i]])
for i in range(Q):
    a, b = map(int, input().split())
    if abs(score[a - 1] - score[b - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
