N, M = map(int, input().split())

answers = []
for a1 in range(1, M + 1):
    for a2 in range(a1 + 10, M + 1):
        for a3 in range(a2 + 10, M + 1):
            answers.append([a1, a2, a3])
print(answers)

answers = []

# for i in range(N - 1):
# i個目の仕切り
