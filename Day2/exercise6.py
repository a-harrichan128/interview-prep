class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            index = 0
            firstZero = len(nums)

            if 0 in nums:
                print("yes")
                while (index <= firstZero):
                    print(index)
                    if (nums[index] == 4):
                        temp = nums.pop(index)
                        print("\t"+str(temp))
                        nums.append(temp)
                        index -= 1
                        if (firstZero == len(nums)):
                            firstZero = len(nums) - 1
                            print("\tset new back")
                        else:
                            firstZero -= 1
                            print("\t"+str(firstZero))
                    index += 1


s1 = Solution()
nums = [1, 0, 4, 0, 0, 0, 4, 3, 1, 2, 2]
s1.moveZeroes(nums)
print(nums)
print("done")
