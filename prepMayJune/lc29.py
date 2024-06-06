'''
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestUniqueSubstring(s):
    mp=set()
    i,j=0,0
    mx=0
    while j<len(s):
        if s[j] in mp:
            mx=max(mx,len(mp))
            while s[j] in mp:
                mp.remove(s[i])
                i+=1
        mp.add(s[j])
        print(mp,mx)
        j+=1
    return max(mx,len(mp))
s="pwwkew"
print(lengthOfLongestUniqueSubstring(s))