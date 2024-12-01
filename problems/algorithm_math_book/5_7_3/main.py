N = int(input())
A = list(map(int, input().split()))
# print(A)
A.sort(reverse=True)
# print(A)

answer = 0
for i, a in enumerate(A):
    # print(i, a)
    index = i + 1
    answer += (N - 2 * index + 1) * a
    # print(answer)
print(answer)
