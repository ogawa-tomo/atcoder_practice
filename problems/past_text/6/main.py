# https://atcoder.jp/contests/past201912-open/tasks/past201912_e

def main():
    N, Q = map(int, input().split())

    # グラフを作る
    graph = []
    for _ in range(N):
        g = ['N'] * N
        graph.append(g)
    # print(graph)
    for _ in range(Q):
        s = list(map(int, input().split()))
        
        # フォロー
        if s[0] == 1:
            follower = s[1] - 1
            followee = s[2] - 1
            graph[follower][followee] = 'Y'

        # フォロー全返し
        if s[0] == 2:
            user = s[1] - 1
            for i in range(N):
                # iさんがuserをフォローしていたら、userはiさんをフォローする
                if graph[i][user] == 'Y':
                    graph[user][i] = 'Y'
        
        # フォローフォロー
        if s[0] == 3:
            a = s[1] - 1
            # aがフォローしているひと
            a_followees = []
            for i in range(N):
                if graph[a][i] == 'Y':
                    a_followees.append(i)
            # aがフォローしているすべてのxに対し、
            for x in a_followees:
                x_followees = []
                for i in range(N):
                    if graph[x][i] == 'Y':
                        x_followees.append(i)
                # xがフォローしているすべてのyに対して、
                for y in x_followees:
                    # aがyをフォローする（yがa自身だったときを除く）
                    if a != y:
                        graph[a][y] = 'Y'
    for row in graph:
        print(''.join(row))

main()
