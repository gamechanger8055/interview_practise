def targetSum(arr,target):
    n = len(arr)
    neg_sum=0
    for i in range(n):
        if arr[i]<0:
            neg_sum+=arr[i]
    for i in range(n):
        #print(arr,neg_sum)
        if arr[i]<0:
            arr[i]=0
        if arr[i]>abs(neg_sum):
            arr[i]+=neg_sum
            #neg_sum=0
            break
        else:
            if neg_sum<0 and arr[i]>0:
                print(neg_sum)
                neg_sum+=arr[i]
                arr[i]=0
    print(arr)
    dp = [[False for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    #print(dp)
    for i in range(1, n + 1):
        for j in range(1,target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]
arr = [3, -5, -1,8,7]
target = 12
print(targetSum(arr,target))