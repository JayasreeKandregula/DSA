#Bubble sort - push the macimum element to last by adjacent swaps

def bubbleSort(nums):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]> nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print(nums)
nums = [10,5,7,1,9,2]
bubbleSort(nums)