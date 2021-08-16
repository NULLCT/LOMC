from collections import deque

N, Q = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N - 1)]
a, b = [list(i) for i in zip(*ab)]

G = [[] for _ in range(N)]
for i in range(N - 1):
    G[a[i] - 1].append(b[i])
    G[b[i] - 1].append(a[i])

start = 1
q = deque()
inf = 10**9
board = [0] * N
w_tmp = -1

q.append(start)
board[start - 1] = 1
while q:
    w = q.popleft()
    for num in G[w - 1]:
        if board[num - 1] != 0:
            continue
        if board[w - 1] == 1:
            board[num - 1] = 2
        if board[w - 1] == 2:
            board[num - 1] = 1
        q.append(num)
    w_tmp = w

for _ in range(Q):
    start, end = map(int, input().split())
    if board[start - 1] == board[end - 1]:
        print('Town')
    else:
        print('Road')
