n = int(input())
for i in range(n):
    x = int(input())
    # 안의 순서는 [0 개수, 1 개수]
    dp = [[1, 0], [0, 1]]
    for j in range(2, x + 1):
        dp.append([dp[j - 1][0] + dp[j - 2][0], dp[j - 1][1] + dp[j - 2][1]])
    print((dp[x][0]), (dp[x][1]))
