import sys
from collections import deque

bitlen = ((10**5).bit_length()) + 1
input = sys.stdin.readline  #ちょっと高速化しないときつい


def befsearch(double, start, k):  #double行列内でstartからk個前の頂点を抽出
    piv = start
    for i in range(bitlen):
        if (k >> i) & 1:
            piv = double[i][piv]
            if piv == -1:  #根の根に到達してたらbreakしないとバグる(ゆるさねぇ)(l[-1]=l[len(l)-1])
                break
    return piv


N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
dirtree = [[] for _ in range(N)]
#まずnondirtreeを構成
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
d = deque()
depth = [0] * N
d.append(0)  #0を根とする
seen = [0] * N
double = [[-1 for _ in range(N)] for _ in range(bitlen)]

#根つき木dirtreeを構成
while len(d) > 0:
    v = d.popleft()
    seen[v] = 1
    for j in tree[v]:
        if (seen[j] == 0):
            dirtree[v].append(j)
            d.append(j)
            depth[j] = depth[v] + 1
            double[0][j] = v

#double[i][j]=「根つき木の頂点jから2**i回上に遡った時の点」としてダブリング、根(0)の根として-1を設定
for i in range(1, bitlen):
    for j in range(N):
        bef = double[i - 1][j]
        if bef == -1:
            double[i][j] = -1
        else:
            double[i][j] = double[i - 1][bef]

for _ in range(Q):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    da = depth[a]
    db = depth[b]

    #二点からLCAに遡るために必要な距離を二分探査
    #手順
    #1.両方の深さを浅い方に揃える
    #2.(ここで0遡ると絶対祖先にならず、無限に遡ると祖先になることを考えて)
    #3.祖先になる遡り数の最小を探査すればよいということになる


    def is_ok(arg):
        #片方深いのがある時は深さを浅い方に揃えてからbefsearch
        if da > db:
            pi = befsearch(double, a, arg + (da - db))
            pj = befsearch(double, b, arg)
        else:
            pi = befsearch(double, a, arg)
            pj = befsearch(double, b, arg + (db - da))
        return (pj == pi)  #祖先になるかの真理値

    def mgr_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    num = mgr_bisect(-1, 10**5 + 10)  #浅い点から祖先に到達するまでの最小距離をbisect
    #浅い方からnumだけ遡った点がLCA
    if depth[a] < depth[b]:
        pans = befsearch(double, a, num)
    else:
        pans = befsearch(double, b, num)
    pathlength = depth[a] + depth[b] - 2 * depth[pans]
    if pathlength % 2 == 0:
        print("Town")
    else:
        print("Road")
    #print(depth[a]+depth[b]-2*depth[pans]+1)           #2点の距離は(aの深さ)+(bの深さ)-2*(aとbのLCAの深さ)であり、それに1を足したものが明らかに答え
