import sys

input = lambda: sys.stdin.readline()[:-1]
ni = lambda: int(input())
na = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10**7)
yes = lambda: print("yes")
Yes = lambda: print("Yes")
no = lambda: print("no")
No = lambda: print("No")
#######################################################################

n, q = na()
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = na()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

d = [0]
dp = [-1 for i in range(n)]
dp[0] = 0
while d:
    e = d.pop()
    for i in g[e]:
        if dp[i] == -1:
            dp[i] = dp[e] ^ 1
            d.append(i)

for i in range(q):
    c, d = na()
    c -= 1
    d -= 1
    if dp[c] ^ dp[d]:
        print("Road")
    else:
        print("Town")
