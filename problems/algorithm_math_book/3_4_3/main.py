# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_y
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ex = 0
for i in range(N):
    ex += (1 / 3) * A[i] + (2 / 3) * B[i]

print(ex)
