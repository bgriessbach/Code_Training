class Solution(object):
    def singleNumber(self, nums):
        mydict={}
        for item in nums:
            if item in mydict.keys():
                mydict[item]=2
            else:
                mydict[item]=1
        for item in mydict.keys():
            if mydict[item]==1:
                return item
//**Second way using set**//

class Solution(object):
    def singleNumber(self, nums):
        myset = set()
        for item in nums:
            if item not in myset:
                myset.add(item)
            else:
               myset.remove(item)
        return myset.pop()
