def subset_sum(weight,target):
    N=len(weight)
    dp = [[False] * (target + 1) for _ in range(N + 1)]
    for i in range(N+1):
        dp[i][0]=True

    for i in range(1,N+1):
        for j in range(1,target+1):
            if weight[i-1]<=j:
                dp[i][j]=dp[i-1][j-weight[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[N][target]

arr=[1,-2,5,-3,8]
target=11
print(subset_sum(arr,target))

def subsetSumWithNegativeNumbers(arr,target):
    #arr.sort()
    neg=0
    write_index=0
    for i in range(len(arr)):
        if arr[i]<0:
            neg+=arr[i]
        else:
            if neg<0:
                arr[i]+=neg
                if arr[i]>=0:
                    neg=0
                else:
                    neg=arr[i]
                    arr[i]=0




