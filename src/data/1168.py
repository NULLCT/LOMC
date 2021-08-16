from collections import deque
#from collections import defaultdict as dfd
from sys import stderr

printn = lambda x: print(x, end='')
inn = lambda: int(input())
inl = lambda: list(map(int, input().split()))
inm = lambda: map(int, input().split())
ins = lambda: input().strip()
DBG = True  # and False
BIG = 10**18
R = 10**9 + 7  # 998244353


def ddprint(*args, **kwargs):
    if DBG:
        print(*args, file=stderr, **kwargs)


n, r = inm()
dst = [{} for i in range(n + 1)]
for i in range(n - 1):
    a, b = inm()
    dst[a][b] = dst[b][a] = 1
di = [R] * (n + 1)
q = deque([1])
di[1] = 0
while len(q) > 0:
    x = q.popleft()
    dd = di[x]
    for u in dst[x]:
        if di[u] == R:
            di[u] = dd + 1
            q.append(u)
for i in range(r):
    c, d = inm()
    print('Town' if (di[c] - di[d]) % 2 == 0 else 'Road')
