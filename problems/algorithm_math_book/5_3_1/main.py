import math

H, W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
    exit()
print(math.ceil(H * W / 2))
