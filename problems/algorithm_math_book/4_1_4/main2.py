import math
A, B, H, M = map(int, input().split())

theta_m = 2 * math.pi * (M / 60)
theta_h = 2 * math.pi * ((60 * H + M) / 720)

# 短針の位置
Hx = A * math.cos(theta_h)
Hy = A * math.sin(theta_h)
# 長針の位置
Mx = B * math.cos(theta_m)
My = B * math.sin(theta_m)

print(math.sqrt((Hx - Mx)**2 + (Hy - My)**2))
