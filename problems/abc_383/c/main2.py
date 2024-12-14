from collections import deque

H, W, D = map(int, input().split())
S = []
for _ in range(H):
    s = input()
    S.append([i for i in s])
# print(S)


# class Point:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def __eq__(self, other):
#         return self.i == other.i and self.j == other.j

#     def __repr__(self):
#         return f"({self.i}, {self.j})"


# i,jに加湿器を置いたとき、加湿される床の座標文字列のリスト（i-j）
def humided_by(i, j):
    humided_points = []
    # dist[h, w]: (i, j)から(h, w)への距離
    dist = []
    for _ in range(H):
        dist.append([None] * W)

    queue = deque()
    # queue.append(Point(i, j))
    queue.append([i, j])
    dist[i][j] = 0
    humided_points.append(f"{i}-{j}")
    while len(queue) > 0:
        p = queue.popleft()  # 調べる頂点
        # if dist[p.i][p.j] > D:
        if dist[p[0]][p[1]] > D:
            break
        # 左
        if p.j - 1 >= 0 and S[p[0]][p.j - 1] != "#":
            # 壁でなければ、キューに加える
            queue.append(Point(p.i, p.j - 1))
            dist[p.i][p.j - 1] = dist[p.i][p.j] + 1
            if dist[p.i][p.j] + 1 <= D:
                humided_points.append(f"{p.i}-{p.j - 1}")

        # 上
        if p.i - 1 >= 0 and S[p.i - 1][p.j] != "#":
            queue.append(Point(p.i - 1, p.j))
            dist[p.i - 1][p.j] = dist[p.i][p.j] + 1
            if dist[p.i][p.j] + 1 <= D:
                humided_points.append(f"{p.i - 1}-{p.j}")

        # 右
        if p.j + 1 < W and S[p.i][p.j + 1] != "#":
            queue.append(Point(p.i, p.j + 1))
            dist[p.i][p.j + 1] = dist[p.i][p.j] + 1
            if dist[p.i][p.j] + 1 <= D:
                humided_points.append(f"{p.i}-{p.j + 1}")

        # 下
        if p.i + 1 < H and S[p.i + 1][p.j] != "#":
            queue.append(Point(p.i + 1, p.j))
            dist[p.i + 1][p.j] = dist[p.i][p.j] + 1
            if dist[p.i][p.j] + 1 <= D:
                humided_points.append(f"{p.i + 1}-{p.j}")

    return humided_points


answer = 0
kashitsuki_points = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            kashitsuki_points.append(Point(i, j))
# print(kashitsuki_points)
humided_points = []
for kashitsuki_point in kashitsuki_points:
    humided_points.extend(humided_by(kashitsuki_point.i, kashitsuki_point.j))
# print(humided_points)
# print(set(humided_points))
print(len(set(humided_points)))
