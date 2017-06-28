class Solution(object):
    def longestCommonPrefix(self, strs):
        result=""
        new_list=[]
        for item in strs:
            new_list.append(item.lower().strip())
            
        for combinations in zip(*new_list):
            if len(set(combinations))==1:
                result+=combinations[0]
            else:
                break
        return result
