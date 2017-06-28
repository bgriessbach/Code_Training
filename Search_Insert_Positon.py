class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        if target<nums[0]:
            return 0
        if target>nums.pop():
            return len(nums)+1
        for index in range(len(nums)):
            if index==len(nums)-1:
                return index+1
            if index<len(nums)-1 and nums[index]<target<nums[index+1]:
                return index+1
