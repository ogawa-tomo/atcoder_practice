N, S = map(int, input().split())
A = list(map(int, input().split()))

amari = S % sum(A)
sumA = [0]
A = A * 2
s = 0
for a in A:
    s += a
    sumA.append(s)
# print(sumA)

start = 0  # Aの足し算をするインデックス
end = 1
while start <= 2 * N and end <= 2 * N:
    total = sumA[end] - sumA[start]
    if total == amari:
        print("Yes")
        exit()
    elif total < amari:
        end += 1
    elif total > amari:
        start += 1
print("No")

# if
