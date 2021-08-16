import sys

input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
node = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)
# print(node)

CNT = [-1] * n
CNT[0] = 0
d = deque([0])
while d:
    x = d.popleft()
    for y in node[x]:
        if CNT[y] == -1:
            CNT[y] = 1 - CNT[x]
            d.append(y)

for i in range(q):
    c, d = map(int, input().split())
    print('Town' if CNT[c - 1] == CNT[d - 1] else 'Road')
