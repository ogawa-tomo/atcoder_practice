N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([])
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

num = 0
for i in range(N):
    neighbors = 0
    for j in graph[i]:
        if j < i:
            neighbors += 1
    if neighbors == 1:
        num += 1

print(num)
