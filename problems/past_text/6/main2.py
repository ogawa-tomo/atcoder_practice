def main():
    N, Q = map(int, input().split())

    graph = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(False)
        graph.append(row)
    
    for _ in range(Q):
        query = list(map(int, input().split()))

        a = query[1] - 1

        if query[0] == 1:
            b = query[2] - 1
            graph[a][b] = True
        
        if query[0] == 2:
            for v in range(N):
                if graph[v][a]:
                    graph[a][v] = True
        
        if query[0] == 3:
            to_follow = []
            for v in range(N):
                if graph[a][v]:
                    for w in range(N):
                        if graph[v][w] and w != a:
                            to_follow.append(w)
            for w in to_follow:
                graph[a][w] = True
    
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                print('Y', end='')
            else:
                print('N', end='')
        print()

main()
