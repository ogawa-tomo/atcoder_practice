from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

graph = []
for r in range(R):
    graph.append(list(input()))

queue = deque()
queue.append([sy, sx])
graph[sy][sx] = 0
# print(graph)
while len(queue) != 0:
    current_point = queue.popleft()
    current_point_y = current_point[0]
    current_point_x = current_point[1]
    above = [current_point_y - 1, current_point_x]
    right = [current_point_y, current_point_x + 1]
    left = [current_point_y, current_point_x - 1]
    below = [current_point_y + 1, current_point_x]
    for point in [above, right, left, below]:
        y = point[0]
        x = point[1]
        if graph[y][x] == ".":
            graph[y][x] = graph[current_point_y][current_point_x] + 1
            queue.append(point)
# for r in graph:
#     # print(len(r))
#     print(r)
print(graph[gy][gx])
