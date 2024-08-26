'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

from collections import Counter
def findIfAnagramsExistInString(s1,s2):
    mp=Counter(s1)
    i,j=0,0
    count=0
    k=len(s1)
    while j<len(s2):
        if s2[j] in mp:
            mp[s2[j]]-=1
            if mp[s2[j]]==0:
                count+=1
        if (j-i+1)==k:
            if count==k:
                return True
            if s2[i] in mp:
                if mp[s2[i]]==0:
                    count-=1
                mp[s2[i]]+=1
            i+=1
        j+=1
    return False
s1 = "ab"
s2 = "eidbaooo"
print(findIfAnagramsExistInString(s1,s2))

