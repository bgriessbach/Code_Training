class Solution(object):
    def removeDuplicates(self, nums):
        index=0
        while index<len(nums)-1:
            if nums[index]==nums[index+1]:
                del nums[index]
            else:
                index+=1
