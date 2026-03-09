#Merge sort - divide the array and merge
# Time complexity - O(NlogN base 2)
#space complexity - O(N) - for temp array

def merge(nums, low, mid, high): #O(N)
    temp = []
    left, right = low, mid+1
    while(left<=mid and right<=high):
        if nums[left]<nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while(left<=mid):
        temp.append(nums[left])
        left+=1
    while(right<=high):
        temp.append(nums[right])
        right+=1
    for i in temp:
        nums[low] = i
        low+=1
def mergeSort(nums,low, high):
    if low>=high:
        return
    middle = (low + high )//2
    mergeSort(nums, low, middle) #O(logN)
    mergeSort(nums,middle+1, high)
    merge(nums, low, middle, high)
    return nums
nums = [3,1,2,4,2,1,27,1]
print(mergeSort(nums, 0, len(nums)-1))