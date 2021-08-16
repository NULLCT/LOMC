n, q = map(int, input().split())
peer = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    peer[a].append(b)
    peer[b].append(a)
st = [0 for _ in range(n)]
seen = [0 for _ in range(n)]
seen[0] = 1
now = [0]
cnt = 0
while now:
    cnt += 1
    last = now
    now = []
    for x in last:
        for y in peer[x]:
            if seen[y] == 0:
                seen[y] = 1
                st[y] = cnt
                now.append(y)
#print(st)
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if (st[a] + st[b]) % 2:
        print('Road')
    else:
        print('Town')
