N, D = map(int, input().split())
S = input()

empty_num = 0
cookie_num = 0
for s in S:
    if s == ".":
        empty_num += 1
    else:
        cookie_num += 1
# print(empty_num)
# print(cookie_num)
print(empty_num + D)
