from collections import deque

n, q = map(int, input().split())

branch = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    branch[a - 1].append(b - 1)
    branch[b - 1].append(a - 1)

queue = deque()
check = [False] * n
ans = [0] * n

for i in range(n):
    if not check[i]:
        check[i] = True
        queue.appendleft(i)

    while len(queue) != 0:
        v = queue.pop()

        for i in branch[v]:
            if not check[i]:
                check[i] = True
                queue.appendleft(i)

            ans[i] = 1 if ans[v] == 0 else 0

for i in range(q):
    c, d = map(int, input().split())
    if ans[c - 1] == ans[d - 1]:
        print('Town')
    else:
        print('Road')
