N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
root = [[] for _ in range(N + 1)]
for i in range(N - 1):
    root[ab[i][0]].append(ab[i][1])
    root[ab[i][1]].append(ab[i][0])
arrived = [False] * (N + 1)

flag = [-1] * (N + 1)
flag[1] = False
stack = [1]
while stack:
    label = stack.pop(-1)
    for i in root[label]:
        if not arrived[i]:
            arrived[i] = True
            flag[i] = (not flag[label])
            stack.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    if flag[c] == flag[d]:
        print('Town')
    else:
        print('Road')
