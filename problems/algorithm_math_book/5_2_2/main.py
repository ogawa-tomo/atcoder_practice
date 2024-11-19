N = int(input())
n = N + 1
# nが2で割り切れれば後手の勝ち
while n > 1:
    n /= 2
if n == 1:
    print("Second")
else:
    print("First")
