import sys

input = sys.stdin.readline
f = lambda: map(int, input().split())
n, Q = f()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = f()
    g[a - 1] += [b - 1]
    g[b - 1] += [a - 1]
B = [-1] * n
B[0] = 0
q = [0]
while q:
    v = q.pop()
    b = B[v] ^ 1
    for c in g[v]:
        if B[c] < 0:
            B[c] = b
            q += [c]
ans = []
for _ in range(Q):
    c, d = f()
    ans += [['Town', 'Road'][B[c - 1] ^ B[d - 1]]]
print(*ans, sep='\n')
