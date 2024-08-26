def knapsack_bottomup(W, weight, profit, N):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if weight[i-1]<=j:
                dp[i][j]=max(profit[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[N][W]

N = 3
W = 50
profit = [60, 100, 120]
weight = [10, 20, 30]
dp = [[-1] * (W + 1) for _ in range(N + 1)]
print(knapsack_bottomup(W, weight, profit, N))