N, K = map(int, input().split())
S = input()
# S = [int(s) for s in S]
# print(S)
s0 = [] # 0の固まりを順番に入れたもの
s1 = [] # 1の固まりを順番に入れたもの


current_mode = None
first_mode = None
current_str_arr = []
for i in range(N):
    if i == 0:
        current_mode = S[i]
        first_mode = current_mode
    if S[i] == '0':
        if current_mode == '0':
            current_str_arr.append('0')
        else:
            # モードが1から0に切り替わる
            s1.append(current_str_arr)
            current_str_arr = ['0']
            current_mode = '0'
    if S[i] == '1':
        if current_mode == '1':
            current_str_arr.append('1')
        else:
            # モードが0から1に切り替わる
            s0.append(current_str_arr)
            current_str_arr = ['1']
            current_mode = '1'
    if i == N - 1:
        if current_mode == '0':
            s0.append(current_str_arr)
        else:
            s1.append(current_str_arr)

# print(s0)
# print(s1)

ans_arr = []
max_len = max(len(s0), len(s1))
if first_mode == '0':
    for i in range(max_len):
        if i == K - 1:
            ans_arr.append(s1[i])
            ans_arr.append(s0[i])
        else:
            ans_arr.append(s0[i])
            if i < len(s1):
                ans_arr.append(s1[i])
if first_mode == '1':
    for i in range(max_len):
        if i == K - 2:
            ans_arr.append(s1[i])
            ans_arr.append(s1[i + 1])
            ans_arr.append(s0[i])
        elif i == K - 1:
            if i < len(s0):
                ans_arr.append(s0[i])
        else:
            ans_arr.append(s1[i])
            if i < len(s0):
                ans_arr.append(s0[i])

ans = []
for a in ans_arr:
    ans.append(''.join(a))
print(''.join(ans))






