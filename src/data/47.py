N, Q = map(int, input().split())
length = [-1] * (N + 1)
length[1] = 0

links = [set() for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    links[a].add(b)
    links[b].add(a)

from collections import deque

q = deque()
for x in links[1]:
    q.append([1, x])

while q:
    tmp = q.popleft()
    for x in links[tmp[1]]:
        if x != tmp[0]:
            q.append([tmp[1], x])
        else:
            length[tmp[1]] = length[tmp[0]] + 1

for i in range(Q):
    c, d = map(int, input().split())
    if (length[c] - length[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
