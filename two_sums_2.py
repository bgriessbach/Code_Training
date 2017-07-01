class Solution(object):
    def twoSum(self, numbers, target):
        mydict={}
        mylist=[]
        for index in range(len(numbers)):
            missing=target-numbers[index]
            if missing in mydict.keys():
                mylist.append(mydict[missing])
                mylist.append(index+1)
            else:
                mydict[numbers[index]]=index+1
        return mylist
