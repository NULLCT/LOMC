import heapq

n, q = list(map(int, input().split()))

hq = []
heapq.heapify(hq)
mapDic = dict()
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    if not (a in mapDic.keys()):
        mapDic[a] = set()
    mapDic[a].add(b)
    if not (b in mapDic.keys()):
        mapDic[b] = set()
    mapDic[b].add(a)

for f in mapDic[1]:
    heapq.heappush(hq, (1, f))

dic = dict()
while len(hq) > 0:
    cost, num = heapq.heappop(hq)
    if not (num in dic.keys()):
        dic[num] = cost
        cost += 1
        for num2 in mapDic[num]:
            heapq.heappush(hq, (cost, num2))
    else:
        continue

ansLis = []
for i in range(q):
    c, d = list(map(int, input().split()))
    dis = abs(dic[c] - dic[d])
    if dis % 2 == 0:
        ansLis.append("Town")
    else:
        ansLis.append("Road")

for i in range(q):
    print(ansLis[i])
