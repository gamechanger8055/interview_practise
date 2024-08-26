'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

def dailyTemperatureChange(temp):
    st=[]
    n=len(temp)
    ans=[0]*n
    for i in range(n-1,-1,-1):
        if not st:
            ans[i]=0
        elif st and temp[i]>st[-1][0]:
            while st and temp[i]>st[-1][0]:
                st.pop()
            if not st:
                st.append([temp[i], i])
                ans[i] = 0
            else:
                ans[i]=(st[-1][1]-i)
        else:
            ans[i]=(st[-1][1]-i)
        st.append([temp[i],i])
    return ans

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatureChange(temperatures))