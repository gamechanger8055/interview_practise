'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

def longestPalindromicSubstring(s):
    n=len(s)
    dp=[False]*n
    longest_palindrome=""
    count=0
    max_Length=0
    for i in range(n):
        for j in range(i,-1,-1):
            if s[i]==s[j] or (dp[j+1] and (i-j)<=2):
                dp[j]=True
                count+=1
                if len(s[j:i+1])>max_Length:
                    max_Length=len(s[j:i+1])
                    longest_palindrome=s[j:i+1]
            else:
                dp[j]=False
    return longest_palindrome

print(longestPalindromicSubstring("babad"))


