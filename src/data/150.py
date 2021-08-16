import queue

N, Q = list(map(int, input().split()))

next_towns = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    next_towns[a].append(b)
    next_towns[b].append(a)

questions = []
for i in range(Q):
    question = list(map(int, input().split()))
    questions.append(question)

que = queue.Queue()

marker = [-1] * (N + 1)
marker[1] = 1
que.put(1)

while not que.empty():
    town = que.get()

    for next_town in next_towns[town]:
        if marker[next_town] == -1:
            marker[next_town] = 1 - marker[town]
            que.put(next_town)

for i in range(Q):
    if marker[questions[i][0]] == marker[questions[i][1]]:
        print("Town")
    else:
        print("Road")
