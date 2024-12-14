N = int(input())

amount = 0
T = []
V = []
for i in range(N):
    t, v = map(int, input().split())
    T.append(t)
    V.append(v)

for i in range(N):
    # 減る水
    if i > 0:
        amount = max(amount - (T[i] - T[i - 1]), 0)
    # 増える水
    amount += V[i]

    # print(amount)

print(amount)
