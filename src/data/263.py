#!/usr/bin/env python
# coding: utf-8

# In[9]:

from collections import deque

# In[24]:

N, Q = map(int, input().split())
path = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)

# In[25]:

q = deque([[0, 0]])
mylst = [-1 for _ in range(N)]
while q:
    p, c = q.pop()
    mylst[p] = c
    nxt = path[p]
    for n in nxt:
        if mylst[n] != -1:
            continue
        if c == 0:
            nc = 1
        else:
            nc = 0
        q.append([n, nc])

# In[26]:

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if mylst[c] == mylst[d]:
        print("Town")
    else:
        print("Road")

# In[ ]:
