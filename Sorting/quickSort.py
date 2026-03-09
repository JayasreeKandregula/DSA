# QUick sort - pick a pivot and place in its correct place
# TImecomplexity - O(NlogN)
# space complexity - O(1)

def qs(nums, low, high):
    pivot = nums[low]
    i, j = low+1, high
    while(i<j):
        while(nums[i]<=pivot and i<j):
            i+=1
        while(nums[j]>pivot and j>i):
            j=j-1
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1
    temp = nums[j]
    nums[j] = nums[low]
    nums[low] = temp
    print(nums)
    return  j


def quickSort(nums, low, high):
    if low < high:
        part_index = qs(nums, low, high)
        quickSort(nums, low, part_index-1)
        quickSort(nums, part_index+1, high)
    return nums

nums = [3,1,4,2,1,6,8,2]
print(quickSort(nums, 0, len(nums)-1))
# 3,1,2,4
# 2,1,3,4