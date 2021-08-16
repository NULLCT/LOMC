import queue
import sys

s = sys.stdin.readlines()

n, q = map(int, s[0].split())

adj = [[] for _ in range(n)]
ad = []
for e in s[1:n]:
    a, b = map(int, e.split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
que = queue.Queue()
color = [-1] * n
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in adj[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)
for e in s[n:]:
    c, d = map(int, e.split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
