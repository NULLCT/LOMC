from collections import defaultdict, deque

N, Q = map(int, input().split())
M = N - 1
d = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)

dist = [None] * N
q = deque()

s = 1 - 1  # スタート
q.append(s)
dist[s] = 0

while len(q) != 0:
    From = q.popleft()
    for To in d[From]:
        if dist[To] == None:
            q.append(To)
            dist[To] = dist[From] + 1
#print(dist)
for q in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
