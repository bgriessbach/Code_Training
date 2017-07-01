class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums)<2:
            return False
        myset=set()
        for item in nums:
            if item in myset:
                return True
            else:
                myset.add(item)
        return False
