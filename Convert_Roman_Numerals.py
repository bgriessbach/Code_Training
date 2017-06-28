class Solution(object):
    def romanToInt(self, s):
        mydict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        reverse=s[::-1]
        result=0
        index=0
        while index<=len(reverse)-1:
            if  index<len(reverse)-1 and mydict[reverse[index]]<=mydict[reverse[index+1]]:
                result+= mydict[reverse[index]]
                index+=1
            elif index==len(reverse)-1:
                 result+= mydict[reverse[index]]
                 index+=1
            else:
                result+=mydict[reverse[index]]-mydict[reverse[index+1]]
                index+=2
        return result
