# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        tur=head
        hare=head
        while hare.next:
            if hare.next.next==None:
                return False
            tur=tur.next
            hare=hare.next.next
            if tur.val==hare.val:
                return True
        return False
