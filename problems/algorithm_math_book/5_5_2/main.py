N = int(input())
a = []
b = []
c = []
for _ in range(N):
    a_, b_, c_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)

candidates = []
# 候補を出す
for i in range(N):
    # 端点
    x = c[i] / a[i]
    candidates.append([x, 0])
    y = c[i] / b[i]
    candidates.append([0, y])

# 内点
for i in range(N - 1):
    for j in range(i + 1, N):
        a1 = a[i]
        b1 = b[i]
        c1 = c[i]
        a2 = a[j]
        b2 = b[j]
        c2 = c[j]
        if a1 * b2 - a2 * b1 == 0:
            continue
        x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
        y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
        if x < 0 or y < 0:
            continue
        candidates.append([x, y])

answer = 0
for candidate in candidates:
    x = candidate[0]
    y = candidate[1]
    # 条件チェック
    ok = True
    for i in range(N):
        a1 = a[i]
        b1 = b[i]
        c1 = c[i]
        if a1 * x + b1 * y > c1:
            ok = False
            break
    if ok:
        answer = max(answer, x + y)

print(answer)
