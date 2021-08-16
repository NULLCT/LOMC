import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split(' '))

seen = [False for _ in range(N)]

roads = [[] for _ in range(N)]
score = [0 for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split(' '))
    roads[a - 1].append(b)
    roads[b - 1].append(a)
Q_list = []
for i in range(Q):
    c, d = map(int, input().split(' '))
    Q_list.append((c, d))


def dfs(city):
    for subcity in roads[city - 1]:
        if seen[subcity - 1] != True:
            score[subcity - 1] += (1 + score[city - 1])
            seen[subcity - 1] = True
            dfs(subcity)
    return 0


seen[0] = True
dfs(1)

for i, j in Q_list:

    if abs(score[i - 1] - score[j - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
