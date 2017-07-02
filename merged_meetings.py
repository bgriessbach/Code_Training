class Solution(object):
    def mergeMeetings(self, mylist):
    	mylist=[[1,3], [4,6], [3,7], [8,10]]
    	mylist=sorted(mylist)
		  merged_list=[mylist[0]]
		  for start, finish in mylist[1:]:
			  merged_start,merged_finish=merged_list[-1]
			  if start<=merged_finish:
				  if finish>merged_finish:
					  merged_list[-1][1]=finish
			  else:
				  merged_list.append((start,finish))
		  return merged_list
