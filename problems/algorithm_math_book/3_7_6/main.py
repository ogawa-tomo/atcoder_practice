N = int(input())
A = list(map(int, input().split()))

p = [None] * N
for i in range(N):
    if i == 0:
        p[0] = A[0]
    elif i == 1:
        p[1] = max(p[0], A[1])
    else:
        p[i] = max(p[i - 2] + A[i], p[i - 1])
print(max(p[N - 2], p[N - 1]))
