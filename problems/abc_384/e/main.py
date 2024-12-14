H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P -= 1
Q -= 1
# S[i][j]: マス(i, j)にいるスライムの強さ
S = []
for _ in range(H):
    s = list(map(int, input().split()))
    S.append(s)
# print(S)


class Point:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.strength = S[i][j]


class Takahashi:
    def __init__(self, p: Point):
        self.points = [p]
        # exisiting_points[i][j]: (i, j)に高橋くんがいるか
        self.existing_points = []
        for _ in range(H):
            self.existing_points.append([False] * W)
        self.existing_points[p.i][p.j] = True
        self.strength = p.strength
        self.surrounded_points: list[Point] = []
        # 上
        if p.i - 1 >= 0:
            self.surrounded_points.append(Point(p.i - 1, p.j))
        # 左
        if p.j - 1 >= 0:
            self.surrounded_points.append(Point(p.i, p.j - 1))
        # 右
        if p.j + 1 < W:
            self.surrounded_points.append(Point(p.i, p.j + 1))
        # 下
        if p.i + 1 < H:
            self.surrounded_points.append(Point(p.i + 1, p.j))

    def self_exists(self, i, j):
        return self.existing_points[i][j]

    # def surrounded_points(self) -> list[Point]:
    #     points: list[Point] = []
    #     for p in self.points:
    #         # 上
    #         i = p.i - 1
    #         j = p.j
    #         if i >= 0 and not self.self_exists(i, j):
    #             points.append(Point(i, j))
    #         # 左
    #         i = p.i
    #         j = p.j - 1
    #         if j >= 0 and not self.self_exists(i, j):
    #             points.append(Point(i, j))
    #         # 右
    #         i = p.i
    #         j = p.j + 1
    #         if j < W and not self.self_exists(i, j):
    #             points.append(Point(i, j))
    #         # 下
    #         i = p.i + 1
    #         j = p.j
    #         if i < H and not self.self_exists(i, j):
    #             points.append(Point(i, j))
    #     return points

    def kyuushuu(self) -> bool:
        # candidates: list[Point] = []
        p = None
        print(len(self.surrounded_points))
        # for i, point in enumerate(self.surrounded_points):
        for i in range(len(self.surrounded_points)):
            # print(i)
            point = self.surrounded_points[i]
            if point.strength < self.strength / X:
                p = point
                self.surrounded_points.pop(i)
                break
        # print("hoge")
        print(len(self.surrounded_points))
        # exit()
        if p is None:
            return False
        self.points.append(p)
        self.existing_points[p.i][p.j] = True
        self.strength += p.strength

        # 上
        i = p.i - 1
        j = p.j
        if i >= 0 and not self.self_exists(i, j):
            self.surrounded_points.append(Point(i, j))
        # 左
        i = p.i
        j = p.j - 1
        if j >= 0 and not self.self_exists(i, j):
            self.surrounded_points.append(Point(i, j))
        # 右
        i = p.i
        j = p.j + 1
        if j < W and not self.self_exists(i, j):
            self.surrounded_points.append(Point(i, j))
        # 下
        i = p.i + 1
        j = p.j
        if i < H and not self.self_exists(i, j):
            self.surrounded_points.append(Point(i, j))

        return True


takahashi = Takahashi(Point(P, Q))
while True:
    result = takahashi.kyuushuu()
    if not result:
        break
print(takahashi.strength)
