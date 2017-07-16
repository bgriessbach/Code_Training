class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return None
        maxSum=nums[0]
        curSum=0
        for item in nums:            
            curSum+=item
            if curSum>maxSum:
                maxSum=curSum
            if curSum<0:
                curSum=0
        return maxSum
