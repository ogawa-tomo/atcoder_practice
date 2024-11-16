# 隣接リストを使った解法

def main():
    N, M, Q = map(int, input().split())
    # N*0の2次元配列を作る
    graph = [[] for _ in range(N)]
    # print(graph)

    # M本の辺を受け取る
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        # 頂点uからvへ辺がある
        graph[u].append(v)
        # 頂点vからuへ辺がある
        graph[v].append(u)
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

            for i in graph[x]:
                # 頂点xに隣接している頂点をC[x]に変える
                C[i] = C[x]

        if query[0] == 2:
            x = query[1]
            y = query[2]
            x -= 1
            print(C[x])
            C[x] = y

main()
