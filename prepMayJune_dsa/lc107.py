'''
Given an array of meeting time meetings consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
'''

def meetingRooms(meetings):
    meetings.sort()
    for i in range(1, len(meetings)):
        if meetings[i][0]<meetings[i-1][1]:
            return False
    return True

meetings=[[7,10],[2,4]]
print(meetingRooms(meetings))