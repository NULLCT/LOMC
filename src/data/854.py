import sys
import queue

sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
L = N - 1

adj = [[] for i in range(N)]

for i in range(L):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

node = [-1] * N
node[0] = 0

q = queue.Queue()
q.put(0)
while not q.empty():
    current = q.get()
    for next in adj[current]:
        if node[next] == -1:
            if node[current] == 0:
                node[next] = 1
            else:
                node[next] = 0
            q.put(next)

for i in range(Q):
    c, d = map(int, input().split())
    if node[c - 1] == node[d - 1]:
        print("Town")
    else:
        print("Road")
