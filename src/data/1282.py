N, Q = map(int, input().split())

I = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    I[a].append(b)
    I[b].append(a)


def derive_parity(I):
    s = 0
    task = [s]
    parity = [-1] * N
    parity[s] = 0
    vis = [False] * N
    vis[s] = True
    while task:
        p = task.pop()
        for q in I[p]:
            if vis[q]: continue
            vis[q] = True
            parity[q] = 1 ^ parity[p]
            task.append(q)
    return parity


parity = derive_parity(I)

for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    if parity[p] == parity[q]:
        print("Town")
    else:
        print("Road")
