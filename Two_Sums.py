from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        mydict=defaultdict(list)
        for index in range (len(nums)):
            difference=target-nums[index]
            if difference in mydict.keys() and len(mydict[difference])>0:
                position=mydict.pop(difference)[0]
                if index<position:
                    return index, position
                else:
                    return position, index
            else:
                mydict[nums[index]].append(index)
