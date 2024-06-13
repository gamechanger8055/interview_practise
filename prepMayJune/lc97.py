'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

def countPalindromicSubstrings(s):
    n = len(s)
    dp = [False] * n
    #longest_palindrome = ""
    count = 0
    #max_Length = 0
    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == s[j] or (dp[j + 1] and (i - j) <= 2):
                dp[j] = True
                count += 1
                # if len(s[j:i + 1]) > max_Length:
                #     max_Length = len(s[j:i + 1])
                #     longest_palindrome = s[j:i + 1]
            else:
                dp[j] = False
    return count

print(countPalindromicSubstrings("aaa"))