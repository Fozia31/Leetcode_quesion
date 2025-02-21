# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        slow = head
        
        while slow :
            new = ListNode(slow.val)
            new.next = dummy.next
            dummy.next = new
            slow = slow.next
        return dummy.next

        