import math

def dist(x, y):
    return math.sqrt(x ** 2 + y ** 2)

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

distance = dist(x1 -x2, y1 - y2)

if distance > r1 + r2:
    print(5)
    exit()

if distance == r1 + r2:
    print(4)
    exit()

if r1 > r2:
    bigger_r = r1
    smaller_r = r2
else:
    bigger_r = r2
    smaller_r = r1

if distance + smaller_r < bigger_r:
    print(1)
    exit()

if distance + smaller_r == bigger_r:
    print(2)
    exit()

print(3)

