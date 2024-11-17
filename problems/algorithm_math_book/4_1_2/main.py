import math

def dist(x, y):
    return math.sqrt(x ** 2 + y ** 2)

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

answer = None
for i in range(N - 1):
    for j in range(i + 1, N):
        d = dist(points[i][0] - points[j][0], points[i][1] - points[j][1])
        if i == 0 and j == 1:
            answer = d
        else:
            answer = min(answer, d)

print(answer)



