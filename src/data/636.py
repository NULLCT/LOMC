N, Q = map(int, input().split())
Roads = []
Ables = [[] for i in range(N)]  #i番目のlistはi番目の街から行ける場所のリスト
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Ables[a].append(b)
    Ables[b].append(a)

nows = {0}
count = 1
odd = set()
even = set()
done = set()
even.add(0)
while True:
    goto = set()
    for now in nows:
        done.add(now)
        for to in Ables[now]:
            goto.add(to)
    nows = goto - done
    for now in nows:
        if count % 2 == 0:
            even.add(now)
        else:
            odd.add(now)
    count += 1
    if len(nows) == 0:
        break


def PrintAns(c, d):
    if (c in odd and d in odd) or (c in even and d in even):
        print("Town")
    else:
        print("Road")


for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    PrintAns(c, d)
