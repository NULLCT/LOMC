import sys

input = sys.stdin.readline
import math
import copy
import bisect
import collections
from collections import deque
from collections import defaultdict

n, q = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

que = deque([0])
dist = [-1] * n
dist[0] = 0
while que:
    check = que.popleft()
    for i in tree[check]:
        if dist[i] == -1:
            dist[i] = dist[check] + 1
            que.append(i)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
