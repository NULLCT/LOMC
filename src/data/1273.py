from collections import deque

N, Q = [int(hoge) for hoge in input().split()]
NextList = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = [int(hoge) - 1 for hoge in input().split()]
    NextList[a].append(b)
    NextList[b].append(a)
isBlack = [-1 for _ in range(N)]
BFS = deque([0])  #queue,append,popleft
isBlack[0] = 0
while BFS:
    curpos = BFS.popleft()
    curcolor = isBlack[curpos]
    for togo in NextList[curpos]:
        if isBlack[togo] == -1:
            isBlack[togo] = 1 - curcolor
            BFS.append(togo)
for q in range(Q):
    c, d = [int(hoge) for hoge in input().split()]
    if isBlack[c - 1] == isBlack[d - 1]:
        print("Town")
    else:
        print("Road")
