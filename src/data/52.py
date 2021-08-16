from collections import deque

n, q = map(int, input().split())
ab = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)
cd = [list(map(int, input().split())) for i in range(q)]

s = set()
qu = deque()
s.add(0)
qu.append(0)
hugo = [0] * n
while qu:
    here = qu.popleft()
    for i in ab[here]:
        if i not in s:
            s.add(i)
            qu.append(i)
            hugo[i] = (hugo[here] + 1) % 2

for i in cd:
    if hugo[i[0] - 1] == hugo[i[1] - 1]:
        print("Town")
    else:
        print("Road")
