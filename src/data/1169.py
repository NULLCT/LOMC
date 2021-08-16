from collections import deque

N, Q = map(int, input().split())
relation = [[] for _ in range(N)]
reached = {0}
dist = [0] * N
for i in range(N - 1):
    A, B = map(int, input().split())
    relation[A - 1].append(B - 1)
    relation[B - 1].append(A - 1)

odd_nodes = []
even_nodes = []

que = deque([0])
while que:
    tmp = que.popleft()
    for crt in relation[tmp]:
        if crt in reached:
            pass
        else:
            reached.add(crt)
            dist[crt] = dist[tmp] + 1
            que.append(crt)

for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
