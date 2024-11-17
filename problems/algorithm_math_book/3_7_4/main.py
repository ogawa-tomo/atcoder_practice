# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_i


N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]: i番目までのカードを使ったとき、合計をjにできるか
dp = []
for i in range(N):
    dp.append([False for _ in range(S + 1)])
    dp_i = dp[i]
    for j in range(S + 1):
        # dp[0][j]がTrueになるのは、jが0のときか、jがA[0]のとき
        if i == 0:        
            if j == 0 or j == A[0]:
                dp_i[j] = True
        else:
            if dp[i - 1][j] or (j >= A[i] and dp[i - 1][j - A[i]]):
                dp_i[j] = True
        if j == S and dp_i[j]:
            print('Yes')
            exit()
print('No')
