n_str = input()
num_1 = 0
num_2 = 0
num_3 = 0
for letter in n_str:
    if letter == '1':
        num_1 += 1
    if letter == '2':
        num_2 += 1
    if letter == '3':
        num_3 += 1
if num_1 == 1 and num_2 == 2 and num_3 == 3:
    print('Yes')
else:
    print('No')
