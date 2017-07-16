class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1)>m:
            nums1.pop()
        while len(nums2)>n:
            nums2.pop()
        for item in nums2:
            nums1.append(item)
        nums1.sort()
        return
                
