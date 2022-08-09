# Binary Search algorithm

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search1(nums, target, 0, len(nums)-1)

    def search1(self, nums, target, low, high):
        pivotIndex = int(high+low/2) 


        if pivotIndex > high:
            return -1
        elif pivotIndex < low:
            return -1
        elif nums[pivotIndex] == target:
            return pivotIndex
        elif target < nums[pivotIndex]:
            print("left")
            print(low, high)
            return self.search1(nums, target, low, pivotIndex-1)
        else:
            print("high")
            print(low, high)
            return self.search1(nums, target, pivotIndex+1, high)


p1 = Solution()
nums = [-1,0,3,5,9,12]
print(p1.search(nums, 9))
