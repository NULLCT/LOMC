import queue

N, Q = map(int, input().split())
E = {i: set() for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].add(b)
    E[b].add(a)

C = [0] * (N + 1)

_queue = queue.Queue()
C[1] = -1
_queue.put(1)
while not _queue.empty():
    x = _queue.get()
    for y in E[x]:
        if C[y] == 0:
            C[y] = C[x] * -1
            _queue.put(y)
#print(C)

for q in range(Q):
    c, d = map(int, input().split())
    if C[c] == C[d]:
        print("Town")
    else:
        print("Road")
