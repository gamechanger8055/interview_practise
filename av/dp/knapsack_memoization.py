def knapsack_memoization(W,weights,values,n):
    if n==0 or W==0:
        return 0
    if dp[n][W]!=-1:
        return dp[n][W]
    else:
        if weights[n-1]<=W:
            dp[n][W]=max(values[n-1]+knapsack_memoization(W-weights[n-1],weights,values,n-1),knapsack_memoization(W,weights,values,n-1))
        else:
            dp[n][W]=knapsack_memoization(W,weights,values,n-1)
        return dp[n][W]
N = 3
W = 50
profit= [60, 100, 120]
weight= [10, 20, 30]
dp=[[-1]*(W+1) for _ in range(N+1)]
print(knapsack_memoization(W,weight,profit,N))