class Solution(object):
    def lengthOfLastWord(self, s):
        if s.isspace() or len(s)==0:
            return 0
        if " " not in s:
            return len(s)
        reverse=s[::-1]
        reverse=reverse.lstrip()
        index=0
        counter=0
        while index<len(reverse) and reverse[index]!=" ":
            counter+=1
            index+=1
        return counter
