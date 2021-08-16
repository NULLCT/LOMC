from queue import Queue

N, Q = map(int, input().split())
rt = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    rt[A - 1].append(B - 1)
    rt[B - 1].append(A - 1)
q = Queue()
q.put(0)
d = {0: True}
while not q.empty():
    t = q.get()
    for i in rt[t]:
        if i not in d:
            d[i] = not d[t]
            q.put(i)
for _ in range(Q):
    C, D = map(int, input().split())
    print('Town' if d[C - 1] == d[D - 1] else 'Road')
