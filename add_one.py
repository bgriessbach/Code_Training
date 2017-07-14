class Solution(object):
    def plusOne(self, digits):
        length=len(digits)
        temp=1
        index=0
        while temp==1 and (length-1-index)>-1:
            back=length-1-index
            digits[back]= (digits[back]+temp)%10
            if digits[back]==0:
                index+=1
            else:
                temp=0
        if temp==1:
            digits.insert(0, 1)
        return digits
