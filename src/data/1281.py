from collections import deque

n, Q = map(int, input().split())
l = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)
s = [-1 for i in range(n)]
q = deque([0])
s[0] = 0
while len(q):
    x = q.popleft()
    for i in l[x]:
        if s[i] != -1:
            continue
        q.append(i)
        s[i] = s[x] + 1
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (s[c] - s[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
