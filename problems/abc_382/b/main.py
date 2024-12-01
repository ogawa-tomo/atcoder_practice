N, D = map(int, input().split())
S = list(input())
# S[2] = "."
# print(S)
current_index = N - 1
for d in range(D):
    while S[current_index] == ".":
        current_index -= 1
    S[current_index] = "."

print("".join(S))
