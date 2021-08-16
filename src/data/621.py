import queue

go = list(map(int, input().split()))
colors = [-1] * go[0]

l = [[] for _ in range(go[0])]

for i in range(go[0] - 1):
    x = list(map(int, input().split()))
    l[x[0] - 1].append(x[1] - 1)
    l[x[1] - 1].append(x[0] - 1)

que = queue.Queue()
colors[0] = 0
que.put(0)

while not que.empty():
    t = que.get()
    for i in l[t]:
        if colors[i] == -1:
            colors[i] = 1 - colors[t]
            que.put(i)

for i in range(int(go[1])):
    start, end = list(map(int, input().split()))
    if colors[start - 1] == colors[end - 1]:
        print("Town")
    else:
        print("Road")
