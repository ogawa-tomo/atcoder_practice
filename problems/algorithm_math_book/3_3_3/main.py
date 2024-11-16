
def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

n, r = map(int, input().split())
answer = int(factorial(n) / (factorial(n - r) * factorial(r)))
print(answer)

