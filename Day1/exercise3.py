class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        found = -1

        if target < nums[left]:
            return 0
        elif target > nums[right]:
            return len(nums)

        while ((right - left) != 1):
            pivot = int((left + right) / 2)
            if (nums[pivot] == target):
                found = pivot
            elif (nums[pivot] < target):
                right = pivot


s1 = Solution()
nums = [1, 3, 5, 7]
target = 9
print(s1.searchInsert(nums, target))
