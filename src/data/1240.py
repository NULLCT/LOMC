import sys

sys.setrecursionlimit(10**7)


class Tree:
    C, RL = {}, {}
    R, N, D, S, P, T = None, None, None, None, None, None
    TL = None

    def __init__(s, num):
        s.N = num

    def set(s, a, b):
        if a in s.C: s.C[a].append(b)
        else: s.C[a] = [b]
        if b in s.C: s.C[b].append(a)
        else: s.C[b] = [a]

    def makeRank(s, root):
        s.R = [0] * s.N  #各ノードのランク
        s.R[root] = 1
        s.RL[1] = [root]  #各ランクのノード
        s.S = {}  #各ノードの子ノード
        s.P = [-1] * s.N  #各ノードの親ノード
        s.D = 1
        while s.RL[s.D] != []:
            s.D += 1
            s.RL[s.D] = []
            for i in s.RL[s.D - 1]:
                for j in s.C[i]:
                    if s.R[j] == 0:
                        s.R[j] = s.D
                        s.RL[s.D].append(j)
                        if i not in s.S: s.S[i] = [j]
                        else: s.S[i].append(j)
                        s.P[j] = i

    def dfs(s, x, y, r):  #xからyまでの道O(M)
        if x == y:
            return [x]
        for i in s.C[x]:
            if i != r:
                t = s.dfs(i, y, x)
                if t != False:
                    return [x] + t
        return False

    def dist(s, x):  #最遠のノード,距離
        t = [-1] * s.N
        S = [x]
        ans = x
        ansn = 0
        t[x] = 0
        while S != []:
            k = S.pop()
            for i in s.C[k]:
                if t[i] == -1:
                    t[i] = t[k] + 1
                    S.append(i)
                    if t[i] > ansn:
                        ansn = t[i]
                        ans = i
        return ans, ansn

    def getDi(s, x=0):  #直径
        a, _ = s.dfs(x)
        b, ans = s.dfs(a)
        return ans

    def getDeep(s, x):  #xの子孫のうち一番深い深さ
        ans = 0
        if x in s.S:
            for i in s.S[x]:
                ans = max(ans, s.getDeep(i))
            return ans + 1
        else:
            return 0

    def getParent(s, x, n):  #xのn世代前の親
        if n == 0:
            return x
        if s.P[x] == -1:
            return -n
        return s.getParent(s.P[x], n - 1)

    def tour(s):  #オイラーツアー
        x = s.RL[1][0]
        s.T = []  #ツアー
        s.TL = [[] for _ in range(s.N)]  #各ノードの出現位置
        L = [x]
        V = [-1] * s.N
        while L:
            n = L.pop()
            if n < 0:
                x = n * -1 - 1
                s.TL[x].append(len(s.T))
                s.T.append(x)
                continue
            s.TL[n].append(len(s.T))
            s.T.append(n)
            if n in s.S:
                for x in (s.S[n]):
                    L.append(-(n + 1))
                    L.append(x)
        return s.T, s.TL


N, Q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

T = Tree(N)
for a, b in ab:
    T.set(a - 1, b - 1)

T.makeRank(0)
V = T.R

for c, d in cd:
    c -= 1
    d -= 1
    n = V[c]
    m = V[d]
    if abs(n - m) % 2 == 0:
        print("Town")
    else:
        print("Road")
