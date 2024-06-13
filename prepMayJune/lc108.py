'''
Given an array of meeting time meetings consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
'''

import heapq
def meetingRooms2(meetings):
    meetings.sort()
    hp=[]
    for meeting in meetings:
        if hp and meeting[0]<=hp[0]:
            heapq.heappop(hp)
        heapq.heappush(hp,meeting[1]) #adding end time
    return len(hp)

meetings=[[0, 30],[5, 10],[15, 20]]
print(meetingRooms2(meetings))