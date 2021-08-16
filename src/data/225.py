from sys import stdin

nii = lambda: map(int, input().split())
lnii = lambda: list(map(int, input().split()))
from collections import deque

n, q = nii()

tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = nii()
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

que = deque()
que.append(0)

col = [-1 for i in range(n)]

while que:
    x = que.popleft()
    for nx in tree[x]:
        if col[nx] != -1:
            continue
        que.append(nx)
        col[nx] = (col[x] + 1) % 2

for i in range(q):
    c, d = nii()
    c -= 1
    d -= 1
    if col[c] == col[d]:
        print('Town')
    else:
        print('Road')
