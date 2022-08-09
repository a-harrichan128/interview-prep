# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import random


class Solution(object):
    n = random.randint(1,200)
    bad = random.randint(1,n)

    def printValue(self):
        print("n is" + str(self.n) + "\n")
        print("bad is" + str(self.bad) + "\n")


    def isBadVersion(self, n):
        if n >= self.bad:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """     
        left = 1
        right = n

        
        while(left != right):
            pivot = int((left+ right)/2)
            if self.isBadVersion(pivot) == False:
                left = pivot + 1
            elif self.isBadVersion(pivot) == True:
                right = pivot
        return left

    
c1 = Solution()
c1.printValue()
print(c1.firstBadVersion(200))
