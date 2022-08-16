class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        left = 0
        right = len(nums)-1
        sorted = []

        while (left != right):
            leftsq = nums[left] * nums[left]
            rightsq = nums[right] * nums[right]
            if leftsq > rightsq:
                sorted.insert(0,leftsq)
                left += 1
            elif leftsq < rightsq:
                sorted.insert(0,rightsq)
                right -= 1
            elif leftsq == rightsq:
                sorted.insert(0,leftsq)
                left += 1

        sorted.insert(0 , nums[left]*nums[left])

        return sorted


s1 = Solution()
nums = [-5,-3,-2,-1 ,0]
print(s1.sortedSquares(nums))
