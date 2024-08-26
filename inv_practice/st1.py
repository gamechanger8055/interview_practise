from collections import deque
'''
You are given a string expression which consists of several comma separated tokens
enclosed within opening ('{') and closing ('}') curly braces.
The string expression might or might not have a prefix before opening curly brace('{') and
a suffix after closing curly brace ('}').
You have to return a list of strings as output for each comma separated item as shown below in the examples.

Example 1:
Input = "/2022/{jan,feb,march}/report"
Output = "/2022/jan/report"
		 "/2022/feb/report"
		 "/2022/march/report"

Example 2:
Input = "over{crowd,eager,bold,fond}ness"
Output = "overcrowdness"
		 "overeagerness"
		 "overboldness"
		 "overfondness"

Example 3:
Input = "read.txt{,.bak}"
Output = "read.txt"
		 "read.txt.bak"

follow up

If there are less than 2 tokens enclosed within curly braces or incorrect expression
(eg. opening and closing braces not present, only opening brace present,
closing brace present before opening brace etc) return the output same as input

Example 1:
Input: sun{mars}rotation
Output: sun{mars}rotation

Example 2:
Input: minimum{}change
Output: minimum{}change

Example 3 (Incorrect Input):
Input: hello-world
Output: hello-world

Example 4 (Incorrect Input):
Input: hello-{-world
Output: hello-{-world

Example 5 (Incorrect Input):
Input: hello-}-weird-{-world
Output: hello-}-weird-{-world
'''

def solveExperession(s):
    start=end=-1
    for i,char in enumerate(s):
        if char=='{':
            start=i
        if char=='}':
            end=i
    sub=s[start+1:end]
    sub_list=sub.split(",")
    if len(sub_list)<2 or end==-1 or start==-1 or start>=end:
        print(s)
        return
    for item in sub_list:
        print(s[:start]+item+s[end+1:])

def handlingMultipleBrackets(s):
    q=deque([("",s)])
    results=[]
    while q:
        prefix,path=q.popleft()
        if not path:
            results.append(prefix)
            continue
        if path[0]=='{':
            end=path.find('}')
            if end==-1 or len(path[1:end].split(","))<2:
                raise ValueError("Incorrect format")
            for choice in path[1:end].split(","):
                q.append((prefix+choice,path[end+1:]))
        else:
            q.append((prefix+path[0],path[1:]))
    print(results)



s="/2022/{jan,feb,march}/report"
t="over{crowd,eager}ab{bold,fond}ness"
u="read.txt{,.bak}"
v="sun{mars}rotation"
w="minimum{}change"
x="hello-{-world"
y="hello-}-weird-{-world"
z="hello-world"
for char in [s,t,u,v,w,x,y,z]:
    solveExperession(char)
    handlingMultipleBrackets(char)
    print()