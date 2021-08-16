from collections import deque

N, Q = map(int, input().split())
G = []
for _ in range(N):
    G.append([])

for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

D = [-1] * N


def search(s, g):
    Q = deque()
    Q.append([s, 0])
    while len(Q) > 0:
        q, d = Q.popleft()
        if D[q] != -1:
            continue

        D[q] = d
        #if q == g:
        #    return d
        for n in G[q]:
            Q.append([n, d + 1])


search(0, N - 1)
#print(D)

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Town' if abs(D[c] - D[d]) % 2 == 0 else 'Road')
