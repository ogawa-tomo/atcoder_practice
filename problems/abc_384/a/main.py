n_str, c1, c2 = input().split()
N = int(n_str)
S = list(input())

answer = []
for s in S:
    if s != c1:
        answer.append(c2)
    else:
        answer.append(s)

print("".join(answer))
