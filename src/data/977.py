N, Q = map(int, input().split())

path = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
l = [0] * N
for i in range(N):
    if len(path[i]) == 1:
        s = i
        break

flag = -1
l[s] = flag
stack = [s]
unused = [1] * N
unused[s] = 0
while len(stack):
    flag *= -1
    new_stack = []
    for p in stack:
        for np in path[p]:
            if unused[np]:
                unused[np] = 0
                l[np] = flag
                new_stack.append(np)
    stack = new_stack[:]

for i in range(Q):
    c, d = map(int, input().split())
    if l[c - 1] == l[d - 1]:
        print('Town')
    else:
        print('Road')
