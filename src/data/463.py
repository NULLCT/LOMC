import queue

n, q = map(int, input().split())
roads = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    roads[a - 1].append(b)
    roads[b - 1].append(a)

towncolors = [-1] * n
towncolors[0] = 0
que = queue.Queue()
que.put(1)
while not que.empty():
    t = que.get()
    for s in roads[t - 1]:
        if towncolors[s - 1] == -1:
            towncolors[s - 1] = (towncolors[t - 1] + 1) % 2
            que.put(s)

for i in range(q):
    c, d = map(int, input().split())
    if towncolors[c - 1] == towncolors[d - 1]:
        print("Town")
    else:
        print("Road")
