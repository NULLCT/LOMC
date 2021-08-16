from collections import deque

N, Q = map(int, input().split())
link = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    link[a].append(b)
    link[b].append(a)

dist = [-1] * N
dist[0] = 0
query = deque()
query.append(0)
while query:
    pos = query.popleft()
    for nxt in link[pos]:

        if dist[nxt] == -1:

            #            print(f"{pos=}")
            #            print(f"{nxt=}")

            dist[nxt] = dist[pos] + 1
            query.append(nxt)

#print(dist)

for i in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if abs(dist[d] - dist[c]) % 2 == 0:
        print("Town")
    else:
        print("Road")
