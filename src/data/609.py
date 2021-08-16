########失敗＃＃＃＃＃＃＃＃＃＃＃＃

from collections import deque

N, Q = map(int, input().split())
L = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N - 1)]

AB = [[] for _ in range(N)]
for s, t in L:
    AB[s].append(t)
    # 無向グラフ⇔双方向と考える、これに気づけなかった・・・
    AB[t].append(s)
CD = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

# 各街を偶数、奇数で色分けする←これに気づけなかった・・・
D = [-1] * N

dq = deque()
dq.append([0, 0])

while dq:
    cur, dis = dq.popleft()

    if D[cur] != -1:
        continue

    D[cur] = dis

    for t in AB[cur]:
        dq.append([t, (dis + 1) % 2])

for i, j in CD:
    if D[j] - D[i] == 0:
        print('Town')
    else:
        print('Road')
