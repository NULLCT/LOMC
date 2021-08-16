import queue

n, Q = map(int, input().split())
ab = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)

points = [-1] * n
points[0] = 0

q = queue.Queue()
q.put(0)
while not q.empty():
    p = q.get()
    for i in ab[p]:
        if points[i] == -1:
            points[i] = points[p] + 1
            q.put(i)


def ans():
    c, d = map(int, input().split())
    c_depth = points[c - 1]
    d_depth = points[d - 1]
    if abs(c_depth - d_depth) % 2 == 0:
        print('Town')
    else:
        print('Road')


for _ in range(Q):
    ans()
