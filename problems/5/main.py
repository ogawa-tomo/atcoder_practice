def main():
    N, M, Q = map(int, input().split())
    # print(N, M, Q)

    # N * Nの2次元配列を作る
    graph = []
    for _ in range(N):
        graph.append([False] * N)
    # print(graph)

    # M本の辺を受け取る
    for _ in range(M):
        u, v = map(int, input().split())

        # 頂点番号は-1する
        u -= 1
        v -= 1

        graph[u][v] = True
        graph[v][u] = True
    # print(graph)

    # 頂点の色
    C = list(map(int, input().split()))

    for _ in range(Q):
        query = list(map(int, input().split()))
        
        # スプリンクラーを起動するクエリ
        if query[0] == 1:
            x = query[1]
            x -= 1
            print(C[x]) # 頂点xの色を出力

            for i in range(N):
                # 頂点iが頂点xに隣接しているとき
                if graph[x][i]:
                    # 頂点iの色をC[x]に置き換える
                    C[i] = C[x]

        if query[0] == 2:
            x = query[1]
            y = query[2]
            x -= 1
            print(C[x])
            C[x] = y

main()
