import queue

#BFSで街を色分け
N, Q = map(int, input().split())
a = [[] for i in range(N + 1)]

for i in range(N - 1):
    st, ed = map(int, input().split())
    a[st].append(ed)
    a[ed].append(st)

que = queue.Queue()
color = [-1] * (N + 1)
color[1] = 0
que.put(1)

while not que.empty():
    now = que.get()
    for i in a[now]:
        if color[i] == -1:
            color[i] = 1 - color[now]
            que.put(i)

for i in range(Q):
    st, ed = map(int, input().split())
    if color[st] == color[ed]:
        print("Town")
    else:
        print("Road")