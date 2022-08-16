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

        while ((right - left) >= 10):
            print(str(left) + " middle " + str(right))
            pivot = int((left + right) / 2)
            if (nums[pivot] == target):
                found = pivot
            elif (nums[pivot] < target):
                left = pivot
            elif (nums[pivot] > target):
                right = pivot

        while (left <= right):
            if (nums[left] == target):
                found = left
                left = right + 1
            elif (nums[left] < target):
                left = left + 1
            elif (nums[left] > target):
                found = left
                left = right + 1
        return found

s1 = Solution()
nums = [1,4,6,7,8,9]
target = 6
print(s1.searchInsert(nums, target))
