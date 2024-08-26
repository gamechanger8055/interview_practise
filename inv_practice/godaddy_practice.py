'''
Find the number of occurance of String s2 in string s1 and letters of s1 do not need to be consecutive.
      Complete the 'getSubsequenceCount' function below.
      The function is expected to return a LONG_INTEGER.
      The function accepts following parameters:
       1. STRING s1
       2. STRING s2
     // s1 - AB,  s2 -  A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B A B C
     '''

def getSubsequenceCount(s1,s2):
    m,n=len(s1),len(s2)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        dp[0][i]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1] #skip or take s2
            else:
                dp[i][j]=dp[i][j-1] #skip
    return dp[m][n]


s1="AB"
s2="ABABABABABABABABABABABABABABABABABABABABABABC"
print(getSubsequenceCount("gks","geeksforgeeks"))