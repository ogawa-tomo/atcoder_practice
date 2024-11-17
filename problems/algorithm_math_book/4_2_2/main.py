T = int(input())
N = int(input())
LR = []
for _ in range(N):
    L, R = map(int, input().split())
    LR.append([L, R])

# diff[t]: 時刻tに増える従業員の数（符号付き）
diff = [0] * (T + 1)
for i in range(N):
    L = LR[i][0]
    R = LR[i][1]
    diff[L] += 1
    diff[R] -= 1

# num[t]: 時刻t+0.5にいる従業員の数
num = [0] * T
for t in range(T):
    if t == 0:
        num[0] = diff[0]
    else:
        num[t] = num[t - 1] + diff[t]
    print(num[t])
