N = int(input())
a = [None] * N
# print(a)

a[0] = 1
a[1] = 1
for i in range(2, N):
    a[i] = (a[i - 1] + a[i - 2]) % 1000000007
print(a[N - 1])
