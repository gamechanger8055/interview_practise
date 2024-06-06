'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


height = [0,1,0,2,1,0,1,3,2,1,2,1]
def trappingRainWaterA1(height):
    n=len(height)
    left=[0]*n
    right=[0]*n
    left[0]=height[0]
    right[-1]=height[-1]
    res=0
    for i in range(1,n):
        left[i]=max(height[i],left[i-1])
    for i in range(n-2,-1,-1):
        right[i]=max(height[i],right[i+1])
    for i in range(n):
        res+=min(right[i],left[i])-height[i]
    return res

def trappingRainWaterA2(height):
    n=len(height)
    max_left,max_right=0,0
    i,j=0,n-1
    result=0
    while i<j:
        if height[i]<=height[j]:
            if height[i]>max_left:
                max_left=height[i]
            else:
                result+=max_left-height[i]
            i+=1
        else:
            if height[j]>max_right:
                max_right=height[i]
            else:
                result+=max_right-height[j]
            j-=1
    return result

print(trappingRainWaterA1(height))
print(trappingRainWaterA2(height))