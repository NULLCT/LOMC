n, q = map(int, input().split())
ikeru = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ikeru[a - 1].append(b - 1)
    ikeru[b - 1].append(a - 1)

fukasa = [0 for _ in range(n)]
kaisuu = 0
settansaku = set([])
setmada = {0}
kouho = 1

while kouho != 0:
    kaisuu += 1
    for i in list(setmada):
        settansaku.add(i)
        setmada.remove(i)
        kouho -= 1
        for k in ikeru[i]:
            if not k in setmada:
                if not k in settansaku:
                    setmada.add(k)
                    kouho += 1
                    fukasa[k] = kaisuu

for i in range(q):
    c, d = map(int, input().split())
    if (fukasa[c - 1] - fukasa[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
