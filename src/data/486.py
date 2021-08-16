import queue
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
r = [[] for _ in range(N)]
que = queue.Queue()
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    r[a].append(b)
    r[b].append(a)
dep = [-1] * N
dep[0] = 0
que.put(0)
while not que.empty():
    id = que.get()
    for i in r[id]:
        if dep[i] == -1:
            dep[i] = dep[id] + 1
            que.put(i)
col = ['Town', 'Road']
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print(col[(dep[c] - dep[d]) % 2])
