class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        rotation = k 

        if not (len(nums) == 0 or len(nums) == 1):
            while (rotation > len(nums)):
                rotation -= len(nums)
            
            front = len(nums) - rotation

            nums[:] = nums[front:] + nums[:front]



s1 = Solution()
nums = [1,2,3,4,5,6,7]
k=10
s1.rotate(nums,k)
print(nums)
