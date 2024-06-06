'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

#from collections import defaultdict
def groupAnagrams(strs):
    mp={}
    for st in strs:
        curr="".join(sorted(list(st)))
        if curr in mp:
            mp[curr].append(st)
        else:
            mp[curr]=[st]
    l=[]
    for key in mp:
        l.append(mp[key])
    l.sort()
    return l

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))