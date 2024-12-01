N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# うまさをインデックスとして与えたとき、それをたべる人のインデックスを返す
taberuhito = [-2] * (2 * 100000 + 1)
# taberuhito = [-2] * (10)
umasa_max = len(taberuhito)
current_umasa = umasa_max
for i, a in enumerate(A):
    if a <= current_umasa:
        # print(i, a)
        for j in range(a, current_umasa + 1):
            if j >= umasa_max:
                continue
            taberuhito[j] = i
        current_umasa = a - 1

# print(taberuhito)
for b in B:
    print(taberuhito[b] + 1)
