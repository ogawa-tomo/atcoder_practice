def main():
    N = int(input())
    zorome_index = 1
    zorome_num = 1
    while True:
        if zorome_index == N:
            print(zorome_num)
            break
        zorome_num = next(zorome_num)
        zorome_index += 1

# 次のゾロ目を求める
def next(zorome_num):
    # 桁数を求める
    digits = get_digits(zorome_num)

    # 数字を求める
    num = get_number(zorome_num)

    next_num = 1 if num == 9 else num + 1
    next_digit =  digits + 1 if num == 9 else digits

    next = 0
    for i in range(next_digit):
        next += next_num * (10 ** (i))
    return next

def get_digits(n):
    return len((str(n)))

def get_number(n):
    return n % 10

main()
