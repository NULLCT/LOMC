from collections import deque


def graph(n):
    res = [[] for _ in range(n)]
    return res


n, q = map(int, input().split())

g = graph(n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

Q = deque()
check = set()

Q.append(1)
check.add(1)
cnt = 1
A = [0] * (n + 1)
while cnt:
    now = Q.popleft()
    cnt -= 1
    for i in range(len(g[now])):
        x = g[now][i]
        if x in check:
            continue
        Q.append(x)
        cnt += 1
        check.add(x)
        A[x] = A[now] ^ 1

while q:
    x, y = map(int, input().split())
    print('Road' if A[x] ^ A[y] else 'Town')
    q -= 1
