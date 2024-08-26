'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''

def generateParenthesis(n):
    def solve(open,close,path):
        if open==0 and close==0:
            result.append(path)
            return
        if open>0:
            solve(open-1,close,path+'(')
        if close>open:
            solve(open, close-1, path + ')')

    result=[]
    solve(n,n,"")
    return result

print(generateParenthesis(4))
