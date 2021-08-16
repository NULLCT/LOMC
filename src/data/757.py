import sys

sys.setrecursionlimit(3000000)
n, q = map(int, input().split())
H = [[] for j in range(n)]
d = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    H[a - 1].append(b - 1)
    H[b - 1].append(a - 1)
flg = [0] * n
flg[0] = 1


def re(s, we):
    d[s] = we + 1
    for itm in H[s]:
        if flg[itm] == 0:
            flg[itm] = 1
            re(itm, we + 1)


re(0, 0)
for i in range(q):
    cc, dd = map(int, input().split())
    if abs(d[cc - 1] - d[dd - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
