from collections import deque

N, Q = map(int, input().split())
# ab[i]にはiから一歩でいける点が入ります。
ab = [set() for _ in range(N)]
c = []
d = []
for i in range(N - 1):
    holda, holdb = map(lambda x: int(x) - 1, input().split())
    ab[holda].add(holdb)
    ab[holdb].add(holda)
for i in range(Q):
    holdc, holdd = map(lambda x: int(x) - 1, input().split())
    c.append(holdc)
    d.append(holdd)

# 判定するのは町で出会うか道路で出会うかのみです。
# もちろん高橋くんから青木くんへ向かうのと青木くんから高橋くんへ向かのは同じルートを通るので、考えるのはc[i],d[i]の最短距離の間にある町の数が偶数か奇数かということだけです。
# 点1から幅優先探索して全部の点への距離を求めます。そして、任意の二点の距離は点1からの距離の差で与えることができます。

queue = deque([0])
# 発見されたかされてないかを管理します。
seen = N * [False]
seen[0] = True
# dist[i]には0からiまでの最短距離が入ります。
dist = N * [-1]
depth = 0
dist[0] = 0

# 幅優先探索
while len(queue) > 0:
    # まずqueueからひとつpop()します
    now = queue.pop()
    # nowから一歩で行ける点を探索します。
    for nextp in ab[now]:
        if not seen[nextp]:
            queue.appendleft(nextp)
            # queueに追加したら発見済みです。
            seen[nextp] = True
            # このループはすべて同じ深さです。深さはnowの深さ+1で与えます。
            dist[nextp] = dist[now] + 1

# クエリに答えます。
for i in range(Q):
    if abs(dist[c[i]] - dist[d[i]]) % 2 == 1:
        print("Road")
    else:
        print("Town")
