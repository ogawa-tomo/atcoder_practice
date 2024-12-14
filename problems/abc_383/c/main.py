from collections import deque

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

    def to_int(self):
        # return (self.i + 1) * 2 * (self.j + 1) * 3
        return f"{self.i}-{self.j}"


# i,jに加湿器を置いたとき、加湿される床の座標文字列のリスト（i-j）
def humided_by(i, j, initial_set):
    # humided_points = []
    humided_points = initial_set
    # dist[h, w]: (i, j)から(h, w)への距離
    dist = []
    for _ in range(H):
        dist.append([None] * W)

    queue = deque()
    p = Point(i, j)
    queue.append(p)
    # queue.append([i, j])
    dist[i][j] = 0
    # humided_points.append(f"{i}-{j}")
    humided_points.add(p.to_int())
    while len(queue) > 0:
        p = queue.popleft()  # 調べる頂点
        current_dist = dist[p.i][p.j]
        if current_dist > D:
            break
        # 左
        if p.j - 1 >= 0 and S[p.i][p.j - 1] != "#":
            # 壁でなければ、キューに加える
            point = Point(p.i, p.j - 1)
            queue.append(point)
            dist[p.i][p.j - 1] = current_dist + 1
            if current_dist + 1 <= D:
                # humided_points.append(f"{p.i}-{p.j - 1}")
                humided_points.add(point.to_int())

        # 上
        if p.i - 1 >= 0 and S[p.i - 1][p.j] != "#":
            point = Point(p.i - 1, p.j)
            queue.append(point)
            dist[p.i - 1][p.j] = current_dist + 1
            if current_dist + 1 <= D:
                humided_points.add(point.to_int())

        # 右
        if p.j + 1 < W and S[p.i][p.j + 1] != "#":
            point = Point(p.i, p.j + 1)
            queue.append(point)
            dist[p.i][p.j + 1] = current_dist + 1
            if current_dist + 1 <= D:
                # humided_points.append(f"{p.i}-{p.j + 1}")
                humided_points.add(point.to_int())

        # 下
        if p.i + 1 < H and S[p.i + 1][p.j] != "#":
            point = Point(p.i + 1, p.j)
            queue.append(point)
            dist[p.i + 1][p.j] = current_dist + 1
            if current_dist + 1 <= D:
                # humided_points.append(f"{p.i + 1}-{p.j}")
                humided_points.add(point.to_int())

    return humided_points


answer = 0
kashitsuki_points = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            kashitsuki_points.append(Point(i, j))
# print(kashitsuki_points)
humided_points = set()
for kashitsuki_point in kashitsuki_points:
    humided_by(kashitsuki_point.i, kashitsuki_point.j, humided_points)
# print(humided_points)
# print(set(humided_points))
# print(len(set(humided_points)))
print(len(humided_points))
