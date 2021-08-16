import sys

sys.setrecursionlimit(100000)


def scan(s, c):
    if lb[s] == None:
        if c % 2 == 0:
            lb[s] = [0, c]
        else:
            lb[s] = [1, c]
    else:
        if lb[s][1] > c:
            if c % 2 == 0:
                lb[s] = [0, c]
            else:
                lb[s] = [1, c]
        else:
            return
    for i in la[s]:
        scan(i, c + 1)
    return


n, q = map(int, input().split())
la = [[] for _ in range(n + 1)]
lb = [None] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    la[a].append(b)
    la[b].append(a)
scan(1, 0)
for j in range(q):
    c, d = map(int, input().split())
    if lb[c][0] == lb[d][0]:
        print("Town")
    else:
        print("Road")
