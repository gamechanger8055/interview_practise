'''
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''


def palindromePartitioning(s):
    def backtrack(start,path):
        if start==len(s):
            result.append(path[:])
            return
        for i in range(start+1,len(s)+1):
            sub=s[start:i]
            if sub==sub[::-1]:
                path.append(sub)
                #main logic
                backtrack(i,path)
                path.pop()
    result=[]
    backtrack(0,[])
    return result

print(palindromePartitioning("aab"))