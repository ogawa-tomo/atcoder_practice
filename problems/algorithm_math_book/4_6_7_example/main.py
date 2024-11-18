a, b = map(int, input().split())
mod = 1000000007

print(5 << 1)

# 掛け算のたびにあまりをとる方法
# O(b)
# answer = 1
# for _ in range(b):
#     answer = (answer * a) % mod
# print(answer)

# 繰り返し二乗法
# aのb乗をmで割った余り
p = a
answer = 1
for i in range(30):
    # print(b & (1 << i))
    if (b & (1 << i)) != 0:
        # print(p)
        answer = (answer * p) % mod
    p = (p * p) % mod
print(answer)
