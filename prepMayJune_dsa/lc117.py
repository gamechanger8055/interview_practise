'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''

def checkValidParentheses(s):
    low=high=0
    for char in s:
        if char=='(':
            low+=1
            high+=1
        elif char==')':
            low-=1
            high-=1
        elif char=='*':
            low-=1
            high+=1
        if high<0:
            return False
        if low<0:
            low=0
    return low==0

s = "(*))"
print(checkValidParentheses(s))