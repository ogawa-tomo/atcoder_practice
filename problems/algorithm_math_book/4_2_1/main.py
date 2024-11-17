N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = []
for _ in range(M):
    B.append(int(input()) - 1)  # 駅番号を-1する

# D[i]: 駅iまでの累積距離
D = [None] * N
# print(D)
for i in range(N):
    if i == 0:
        D[0] = 0
        continue
    D[i] = D[i - 1] + A[i - 1]

distance = 0
for i in range(M - 1):
    # 駅B[i] から駅B[i + 1]までの距離
    distance += abs(D[B[i]] - D[B[i + 1]])
print(distance)
