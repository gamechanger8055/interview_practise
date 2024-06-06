'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
 return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

def largestAreaOfRectangleInHistogram(height):
    n=len(height)
    maxArea=0
    stack=[]
    for i in range(n):
        start=i
        while stack and stack[-1][0]>height[i]:
            prev_height,prev_index=stack.pop()
            maxArea=max(maxArea,prev_height*(i-prev_index))
            start=prev_index
        stack.append((height[i],start))
        print(stack,maxArea,start)
    for height,index in stack:
        maxArea = max(maxArea, height * (n-index))
    return maxArea

#in nsr if stack empty ans=n and in nsl if stack empty ans=-1
def nsr(height):
    n=len(height)
    stack=[]
    res=[0]*n
    for i in range(n-1,-1,-1):
        if not stack:
            res[i]=n
        elif stack and height[i]<=stack[-1][0]:
            while stack and height[i]<=stack[-1][0]:
                stack.pop()
            if not stack:
                res[i] = n
            else:
                res[i]=stack[-1][1]
        else:
            res[i] = stack[-1][1]
        stack.append((height[i],i))
    return res

def nsl(height):
    n = len(height)
    stack = []
    res = [0] * n
    for i in range(n):
        if not stack:
            res[i] = -1
        elif stack and height[i] <= stack[-1][0]:
            while stack and height[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1][1]
        else:
            res[i] = stack[-1][1]
        stack.append((height[i], i))
    return res
def largestAreaOfRectangleInHistogramAdityaVerma(height):
    nsl_array=nsl(height)
    nsr_array=nsr(height)
    ans=[0]*len(height)
    for i in range(len(height)):
        ans[i]=(nsr_array[i]-nsl_array[i]-1)*height[i]
    return max(ans)


heights = [2, 1, 5, 6, 2, 3]
print(largestAreaOfRectangleInHistogram(heights))
print(largestAreaOfRectangleInHistogramAdityaVerma(heights))