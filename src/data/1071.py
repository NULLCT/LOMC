#author: ankan2526

import math, bisect, heapq, sys

#n,k=map(int,input().split())
n, q = map(int, input().split())
store = {}
for i in range(n - 1):
    x, y = map(int, input().split())
    if x not in store:
        store[x] = []
    if y not in store:
        store[y] = []
    store[x].append(y)
    store[y].append(x)
length = {1: 0}
done = set([1])
queue = [1]
x = 0
while queue:
    x ^= 1
    temp = []
    for i in queue:
        for j in store[i]:
            if j not in done:
                done.add(j)
                temp.append(j)
                length[j] = x
    queue = temp
for i in range(q):
    x, y = map(int, input().split())
    if length[x] ^ length[y]:
        print("Road")
    else:
        print("Town")
