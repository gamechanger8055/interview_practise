# same as 2 sum

def twoSum(nums,target):
    nums.sort()
    l=[]
    i,j=0,len(nums)-1
    while i<j:
        if nums[i]+nums[j]==target:
            l.append((nums[i],nums[j]))
            i+=1
            j-=1
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            i+=1
    return l

nums=[1,2,3,6,4,5]
target=9
print(twoSum(nums,target))