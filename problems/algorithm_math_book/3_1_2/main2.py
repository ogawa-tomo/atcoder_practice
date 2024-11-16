import math
N = int(input())
limit = int(math.sqrt(N))

prime_factors = []
for i in range(2, limit + 1):
    while N % i == 0:
        N /= i
        prime_factors.append(i)

if N >= 2:
    prime_factors.append(int(N))

print(*prime_factors)
    