import collections

n, q = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = [False for i in range(n + 1)]
flag2 = [False for i in range(n + 1)]
queue = collections.deque([1])
while queue:
    test = queue.popleft()
    flag[test] = True
    for i in graph[test]:
        if flag[i] == False:
            queue.append(i)
            if flag2[test] == True:
                flag2[i] = False
            else:
                flag2[i] = True
for i in range(q):
    c, d = map(int, input().split())
    if flag2[c] == flag2[d]:
        print("Town")
    else:
        print("Road")