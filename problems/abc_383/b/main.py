H, W, D = map(int, input().split())
S = []
for _ in range(H):
    s = input()
    S.append([i for i in s])
# print(S)


class Point:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __repr__(self):
        return f"({self.i}, {self.j})"


floor_points = []
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            floor_points.append(Point(h, w))
# print(floor_points)


# i,jに加湿器を置いたとき、加湿される床の座標文字列のリスト（i-j）
def humided_by(i, j):
    humided = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == "." and abs(h - i) + abs(w - j) <= D:
                humided.append(f"{h}-{w}")
    return humided


answer = 0
point_num = len(floor_points)
for p1_index in range(point_num - 1):
    for p2_index in range(p1_index + 1, point_num):
        # 加湿器を置く床の組み合わせ
        p1 = floor_points[p1_index]
        p2 = floor_points[p2_index]
        # print(p1)
        # 加湿器を置いたときに
        humided_by_p1 = humided_by(p1.i, p1.j)
        humided_by_p2 = humided_by(p2.i, p2.j)
        # print(humided_by_p1)
        humided_by_p1_and_p2 = humided_by_p1 + humided_by_p2
        num = len(set(humided_by_p1_and_p2))
        answer = max(num, answer)
print(answer)
