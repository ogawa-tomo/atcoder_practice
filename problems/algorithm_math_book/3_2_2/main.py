# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_p

def gcd(a, b):
    bigger, smaller = [a, b] if a > b else [b, a]
    if smaller == 0:
        return bigger
    return gcd(smaller, bigger % smaller)

N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N - 1):
    a = A[i] if i == 0 else answer
    b = A[i + 1]
    answer = gcd(a, b)

print(answer)


