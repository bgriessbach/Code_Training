# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        current=head
        previous=None
        while current.next:
            previous=current
            if current.val==current.next.val:
                if current.next.next==None:
                    previous.next=None
                else:
                    previous.next=current.next.next
                current=previous
            else:
                current=current.next
        return head
