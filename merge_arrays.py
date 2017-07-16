class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1)>m:
            nums1.pop()
        while len(nums2)>n:
            nums2.pop()
        if len(nums1)==0:
            for item in nums2:
                nums1.append(item)
            return
        start_length=len(nums1)
        index1=0
        index2=0
        while len(nums1)!=len(nums2)+start_length:
            if nums1[index1]>=nums2[index2]:
                nums1.insert(index1 ,nums2[index2])
                index2+=1
            else:
                if len(nums1)>=index1+2:
                    index1+=1
                else:
                    nums1.append(nums2[index2])
                    index2+=1
                
