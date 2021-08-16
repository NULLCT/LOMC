N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N - 1)]
cd = [list(map(int, input().split())) for i in range(Q)]
data = [[] for i in range(N + 1)]
for i in range(N - 1):
    a = ab[i][0]
    b = ab[i][1]
    data[a].append(b)
    data[b].append(a)
dis1 = [-1] * (N + 1)
dis1[1] = 0
deque = [1]
while deque:
    x = deque.pop(0)
    for i in data[x]:
        if dis1[i] == -1:
            dis1[i] = dis1[x] + 1
            deque.append(i)
for i in range(Q):
    p = dis1[cd[i][0]] - dis1[cd[i][1]]
    if p % 2 == 0:
        print("Town")
    else:
        print("Road")
