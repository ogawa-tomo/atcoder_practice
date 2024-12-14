N, R = map(int, input().split())

for _ in range(N):
    D, A = map(int, input().split())
    if D == 1 and 1600 <= R and R <= 2799:
        R += A
    elif D == 2 and 1200 <= R and R <= 2399:
        R += A

print(R)
