'''
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import Counter
def minWindowSubstring(s,t):
    reqd=Counter(t)
    i,j=0,0
    resLen=float('inf')
    res=""
    have=0
    need=len(reqd)
    while j<len(s):
        if s[j] in reqd:
            reqd[s[j]]-=1
            if reqd[s[j]]==0:
                have+=1
        while have==need:
            if (j-i+1)<resLen:
                resLen=(j-i+1)
                res=s[i:j+1]
            if s[i] in reqd:
                if reqd[s[i]] == 0:
                    have -= 1
                reqd[s[i]] += 1
            i+=1
        j+=1
    return res


s = "ADOBECODEBANC"
t = "ABC"
print(minWindowSubstring(s,t))