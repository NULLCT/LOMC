import sys

input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(2 * 10**5 + 10)
write = lambda x: sys.stdout.write(x + "\n")
debug = lambda x: sys.stderr.write(x + "\n")
writef = lambda x: print("{:.12f}".format(x))

### 木の読み込み yomikomi
n, qq = map(int, input().split())
ns = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].append(v)
    ns[v].append(u)
# 深さ優先探索 (巻き戻しあり) dfs tree
q = [(0, -1)]
ds = [0] * n
while q:
    u, prv = q.pop()
    if u < 0:
        # 返るときの処理
        u = ~u
        for v in ns[u]:
            if v == prv:
                continue
            pass
    else:
        q.append((~u, prv))
        for v in ns[u]:
            # 進むときの処理
            if v == prv:
                continue
            q.append((v, u))
            ds[v] = ds[u] + 1
ans = []
for i in range(qq):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (ds[c] + ds[d]) % 2 == 0:
        ans.append("Town")
    else:
        ans.append("Road")
write("\n".join(ans))
