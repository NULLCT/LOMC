import queue

N, Q = map(int, input().split())

road = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

que = queue.Queue()
tree = [-1] * N
tree[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in road[t]:
        if tree[i] == -1:
            tree[i] = 1 - tree[t]
            que.put(i)

q = []
for i in range(Q):
    c, d = map(int, input().split())
    q.append([c, d])

for c, d in q:
    if tree[c - 1] == tree[d - 1]:
        print('Town')
    else:
        print('Road')
