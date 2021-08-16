N, Q = map(int, input().split())
road = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    road[A - 1].append(B - 1)
    road[B - 1].append(A - 1)

que = [0]
color = [-1] * N
color[0] = 0
while len(que) > 0:
    tmp = que.pop(0)
    for i in road[tmp]:
        if color[i] == -1:
            color[i] = 1 - color[tmp]
            que.append(i)

for i in range(Q):
    C, D = map(int, input().split())
    if color[C - 1] == color[D - 1]:
        print("Town")
    else:
        print("Road")
