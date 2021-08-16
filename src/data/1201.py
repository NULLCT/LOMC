def l():
    return list(map(int, input().split()))


from queue import Queue

N, Q = l()
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = l()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

que = Queue()
que.put(0)
odd_even = [-1] * N
odd_even[0] = 0
while not que.empty():
    v = que.get()
    for nv in G[v]:
        if odd_even[nv] != -1: continue
        odd_even[nv] = odd_even[v] ^ 1
        que.put(nv)
# print(odd_even)

for _ in range(Q):
    c, d = l()
    c -= 1
    d -= 1
    if odd_even[c] ^ odd_even[d]:
        print("Road")
    else:
        print("Town")
