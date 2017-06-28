class Solution(object):
    def isValid(self, s):
        mydict={"(":")", "[":"]", "{":"}"}
        mylist=[]
        for item in s:
            if item in mydict.keys():
                mylist.append(mydict[item])
            else:
                if len(mylist)<1 or mylist.pop()!=item:
                    return False
        if len(mylist)!=0:
            return False
        return True
