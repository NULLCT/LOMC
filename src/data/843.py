from collections import deque

N, Q = map(int, input().split())
l = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)

que = deque([(0, 0)])
visited = [10**18] * N
visited[0] = 0
while que:
    q, c = que.popleft()
    for i in l[q]:
        if visited[i] > c + 1:
            visited[i] = c + 1
            que.append((i, c + 1))

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    ans = 'Town'
    num = visited[c] + visited[d]
    if num % 2 != 0:
        ans = 'Road'
    print(ans)
