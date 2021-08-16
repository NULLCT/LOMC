n, q = map(int, input().split())

G = [[] for i in range(n)]

for i in range(n - 1):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

# coloring with bfs
import queue

que = queue.Queue()
que.put(0)
color = [-1 for i in range(n)]
color[0] = 0
while (not (que.empty())):
    par = que.get()
    for ch in G[par]:
        if color[ch] == -1:
            color[ch] = abs(color[par] - 1)
            que.put(ch)

# answer
for i in range(q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    if (color[ci] != color[di]):
        print("Road")
    else:
        print("Town")
