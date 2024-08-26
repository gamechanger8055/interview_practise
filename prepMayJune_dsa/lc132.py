'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

def EditDistances(word1,word2):
    m,n=len(word1),len(word2)
    dp=[[0 for _ in range(n+1)] for j in range(m+1)]
    #insert
    for i in range(m+1):
        dp[i][0]=i
    for i in range(n+1):
        dp[0][i]=i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1] #replace
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    return dp[m][n]

word1 = "intention"
word2 = "execution"
print(EditDistances(word1,word2))