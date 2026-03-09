# Selection Sort - select minimum and swap minimum value with i 
#Time complexity -  O(n^2) - Best/Avg/worst
# Space complexity - O(1) - only 2 variables space

def selectionSort(nums):
    for i in range(0, len(nums)-1):
        min = i
        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                min = j
        if min !=i:
            temp = nums[i]
            nums[i] = nums[min]
            nums[min] = temp
    print(nums)

nums = [10, 1,5,20,3 ,6]
selectionSort(nums)