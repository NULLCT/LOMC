N, Q = map(int, input().split())

connect = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

stack = [1]
state = [-1 for _ in range(N + 1)]
state[1] = 0
red = [[], []]
color = [-1 for _ in range(N + 1)]
while stack:
    s = stack.pop()
    if state[s] == 0:
        color[s] = 0
    if state[s] == 1:
        color[s] = 1
    for i in connect[s]:
        if state[i] != -1:
            continue
        state[i] = 1 - state[s]
        stack.append(i)
    state[s] = 2

for i in range(Q):
    c, d = map(int, input().split())

    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
