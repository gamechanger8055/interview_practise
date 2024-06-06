'''
ou are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

def searchInA2Dmatrix(matrix,target):
    m,n=len(matrix),len(matrix[0])
    left,right=0,n-1
    while left<m and right>=0:
        if matrix[left][right]==target:
            return True
        elif matrix[left][right]>target:
            right-=1
        else:
            left+=1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
print(searchInA2Dmatrix(matrix,target))
