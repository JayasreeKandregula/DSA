# Insertion sort - Insert the element in its correct position in already sorted array
# Time complexity - O(n^2) best/worst/avg time complexity
# space complexity - O(1) 2 variables space
def insertionSort(nums):
    for i in range(1, len(nums)):
        curr = i
        j = i-1
        while j>=0:
            if nums[curr] < nums[j]:
                temp = nums[curr]
                nums[curr] = nums[j]
                nums[j] = temp
                curr = j
            j-=1
    print(nums)
                

nums = [9,1, 5, 3, 8, 1]
insertionSort(nums)