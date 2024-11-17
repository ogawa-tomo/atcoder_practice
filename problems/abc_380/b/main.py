S = input()
s_arr = S.strip('|').split('|')

ans_arr = []
for s in s_arr:
    ans_arr.append(len(s))
print(*ans_arr)
