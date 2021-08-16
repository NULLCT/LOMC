#!/usr/bin/env python3
import sys
import queue

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
#print(G)
que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
#print(que)

while (not que.empty()):
    tmp = que.get()
    #print(tmp)
    for i in G[tmp]:
        if (color[i] == -1):
            color[i] = 1 - color[tmp]
            que.put(i)

for i in range(Q):
    a, b = map(int, input().split())
    if (color[a - 1] == color[b - 1]):
        print("Town")
    else:
        print("Road")
