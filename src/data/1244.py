import sys

input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
node = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)

num = [-1] * n
num[0] = 0
queue = deque([0])
while queue:
    x = queue.popleft()
    for y in node[x]:
        if num[y] == -1:
            num[y] = 1 - num[x]
            queue.append(y)

for i in range(q):
    c, d = map(int, input().split())
    print("Town" if num[c - 1] == num[d - 1] else "Road")
