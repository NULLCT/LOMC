from collections import deque

N, q = map(int, input().split())
l = [[] for i in range(N)]
#print(l)
for i in range(N - 1):
    a, b = map(int, input().split())
    l[a - 1].append(b - 1)
    l[b - 1].append(a - 1)
#print(l)
s, g = 0, N - 1

dis = [0 for i in range(N)]
conf = [True for i in range(N)]

count = 0
d = deque([(s, 0)])

#while sum(cof)!=0:
while len(d) != 0:

    watch, dist = d.popleft()
    conf[watch] = False

    for i in l[watch]:
        S = dis[i]
        if S == 0 and conf[i]:
            dis[i] = dist + 1
            d.append((i, 1 + dist))

#print(dis)
for i in range(q):
    s, g = map(int, input().split())
    if (dis[s - 1] - dis[g - 1]) % 2 == 0:

        print("Town")
    else:
        print("Road")
