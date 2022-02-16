# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) / 2
            
            if isBadVersion(mid):
                latest_bad = mid
                right = mid
            else:
                left = mid + 1 # latest bad we have seen
        
        return int(left)