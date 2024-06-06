#---------knapsack------------------------------
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
def recursive(weights,values,w,n):
    if n==0 or w==0:
        return 0
    if weights[n-1]<=w:
        return max(values[n-1]+recursive(weights,values,w-weights[n-1],n-1),recursive(weights,values,w,n-1))
    else:
        return recursive(weights,values,w,n-1)

def dp(weights,values,w,n):
    dp=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if weights[i-1]<=j:
                dp[i][j]=max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
print(recursive(weights,values,W,len(weights)),dp(weights,values,W,len(values)))


#----------------subset sum------------------------

arr=[2,3,5,6,8,10]
target=10

def countSubsetSum(arr,target):
    n=len(arr)
    dp=[[0 for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    # for i in range(target+1):
    #     dp[0][i]=1
    for i in range(1,n+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

print(countSubsetSum(arr,target))

arr=[1,6,5,11]

def minSubsetSumDiff(arr):
    n = len(arr)
    target=sum(arr)
    dp = [[False for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] =  dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    mn=float('inf')
    print(dp[n-1])
    for i in range(target//2+1):
        if dp[n-1][i]:
            mn=min(mn,abs(2*i-target))
    return mn

print(minSubsetSumDiff(arr))

arr=[1,1,2,3]
diff=1

def CountSubsetWithGivenDiff(arr,diff):
    target=(sum(arr)+diff)//2  #s1+s2 =sum and s1-s2=diff
    n = len(arr)
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    # for i in range(target+1):
    #     dp[0][i]=1
    for i in range(1, n + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]

print(CountSubsetWithGivenDiff(arr,diff))

