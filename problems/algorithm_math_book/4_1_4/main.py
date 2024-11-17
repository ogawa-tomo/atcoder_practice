import math

A, B, H, M = map(int, input().split())

theta_m = 2 * math.pi * (M / 60)
theta_h = 2 * math.pi * ((60 * H + M) / 720)

theta = abs(theta_h - theta_m)
if theta > math.pi:
    theta = 2 * math.pi - theta

C = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(theta))
print(C)
