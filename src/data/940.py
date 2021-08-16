import sys

sys.setrecursionlimit(100000000)

n, q = map(int, input().split())
# inf = float('inf')
# dist = [[inf for _ in range(n+1)] for _ in range(n+1)]
evenorodd = [-1] * (n + 1)
evenorodd[1] = 0
edge = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
done = [0] * (n + 1)


def near_check(n, num):
    # 隣あっているやつを確認していく
    tmp = (num + 1) % 2
    if done[n] == 1:
        return
    done[n] = 1
    for i in edge[n]:
        if evenorodd[i] == -1:
            evenorodd[i] = tmp
            near_check(i, tmp)


near_check(1, 0)

#print(evenorodd)

for i in range(q):
    c, d = map(int, input().split())
    if evenorodd[c] == evenorodd[d]:
        print("Town")
    else:
        print("Road")
